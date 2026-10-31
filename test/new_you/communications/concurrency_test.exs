defmodule NewYou.Communications.ConcurrencyTest do
  use ExUnit.Case, async: false
  import Ecto.Query
  alias Ecto.Adapters.SQL.Sandbox
  alias NewYou.{Communications, Repo}

  test "concurrent handoffs converge on one intent and one envelope" do
    previous = Application.get_env(:new_you, :communications_keyring)

    Application.put_env(:new_you, :communications_keyring, %{
      active: "test",
      keys: %{"test" => :crypto.strong_rand_bytes(32)}
    })

    source = Joken.generate_jti()

    attrs = %{
      source_operation_id: Ash.UUID.generate(),
      source_reference: source,
      destination: "participant@example.test",
      destination_provenance: "identity_challenge_issuance",
      destination_authorized_at: DateTime.utc_now(),
      locale: "en",
      content_item_id: "NEWYOU-CONTENTITEM-VERIFICATION-MESSAGE-EMAIL-ADDRESS",
      content_version_id: "NEWYOU-CONTENTVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-V1",
      translation_version_id:
        "NEWYOU-CONTENTTRANSLATIONVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-EN-V1",
      content_sha256: "a8ceecc466497bd3d79ae9255a7f004b18461a2d6a1791028a68bcb1efd2a072"
    }

    bearer = :crypto.strong_rand_bytes(32)

    on_exit(fn ->
      Sandbox.unboxed_run(Repo, fn ->
        {:ok, %{rows: rows}} =
          Ecto.Adapters.SQL.query(
            Repo,
            "SELECT nonce FROM communications_protected_envelopes WHERE source_reference = $1",
            [source]
          )

        Repo.delete_all(from i in "message_intents", where: i.source_reference == ^source)

        for [nonce] <- rows do
          Repo.delete_all(from n in "communications_envelope_nonces", where: n.nonce == ^nonce)
        end
      end)

      if previous,
        do: Application.put_env(:new_you, :communications_keyring, previous),
        else: Application.delete_env(:new_you, :communications_keyring)
    end)

    task = fn _ ->
      Sandbox.unboxed_run(Repo, fn -> Communications.establish_verification(attrs, bearer) end)
    end

    results =
      1..6 |> Task.async_stream(task, max_concurrency: 6, timeout: 30_000) |> Enum.to_list()

    ids =
      Enum.map(results, fn
        {:ok, {:ok, intent}} -> intent.id
        _ -> :failed
      end)

    assert length(Enum.uniq(ids)) == 1
    refute :failed in ids

    {:ok, %{rows: [[intent_count, envelope_count]]}} =
      Sandbox.unboxed_run(Repo, fn ->
        Ecto.Adapters.SQL.query(
          Repo,
          "SELECT count(*), count(e.message_intent_id) FROM message_intents i LEFT JOIN communications_protected_envelopes e ON e.message_intent_id = i.id WHERE i.source_reference = $1",
          [source]
        )
      end)

    assert intent_count == 1
    assert envelope_count == 1
  end
end
