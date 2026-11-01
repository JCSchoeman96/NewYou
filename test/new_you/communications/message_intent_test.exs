defmodule NewYou.Communications.MessageIntentTest do
  use NewYou.DataCase, async: false

  alias NewYou.Communications

  setup do
    previous = Application.get_env(:new_you, :communications_keyring)

    Application.put_env(:new_you, :communications_keyring, %{
      active: "test",
      keys: %{"test" => :crypto.strong_rand_bytes(32)}
    })

    on_exit(fn ->
      if previous,
        do: Application.put_env(:new_you, :communications_keyring, previous),
        else: Application.delete_env(:new_you, :communications_keyring)
    end)

    :ok
  end

  defp attrs(locale \\ "en") do
    {translation, digest} =
      case locale do
        "en" ->
          {"NEWYOU-CONTENTTRANSLATIONVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-EN-V1",
           "a8ceecc466497bd3d79ae9255a7f004b18461a2d6a1791028a68bcb1efd2a072"}

        "af" ->
          {"NEWYOU-CONTENTTRANSLATIONVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-AF-V1",
           "c3212222fdcd878af6bdc2b17895d4d6cab44e162814e2a8deee10b7fd916494"}
      end

    %{
      source_operation_id: Ash.UUID.generate(),
      source_reference: Joken.generate_jti(),
      destination: "participant@example.test",
      destination_provenance: "identity_challenge_issuance",
      destination_authorized_at: DateTime.utc_now(),
      locale: locale,
      content_item_id: "NEWYOU-CONTENTITEM-VERIFICATION-MESSAGE-EMAIL-ADDRESS",
      content_version_id: "NEWYOU-CONTENTVERSION-VERIFICATION-MESSAGE-EMAIL-ADDRESS-V1",
      translation_version_id: translation,
      content_sha256: digest
    }
  end

  test "exact EN and AF bindings are retained and replay converges" do
    for locale <- ["en", "af"] do
      input = attrs(locale)
      bearer = :crypto.strong_rand_bytes(32)
      {:ok, first} = Communications.establish_verification(input, bearer)
      {:ok, replay} = Communications.establish_verification(input, bearer)
      assert first.id == replay.id
      assert first.locale == locale
      assert first.source_reference == input.source_reference
      assert first.content_item_id == input.content_item_id
      assert first.content_version_id == input.content_version_id
      assert first.translation_version_id == input.translation_version_id
      assert first.content_sha256 == input.content_sha256
      assert first.destination == input.destination
      assert first.destination_provenance == input.destination_provenance
      assert first.dispatch_disposition == :open
      assert first.platform_name == NewYou.platform_name()
      assert first.render_schema == "verification-v1"
      assert first.render_provenance == "application_platform_name"
      assert byte_size(first.render_digest) == 64

      assert {:error, _} =
               Communications.establish_verification(
                 %{input | locale: if(locale == "en", do: "af", else: "en")},
                 bearer
               )

      assert {:error, _} =
               Communications.establish_verification(
                 %{input | content_sha256: String.duplicate("0", 64)},
                 bearer
               )

      {:ok, newer} =
        Communications.establish_verification(
          %{input | source_reference: Joken.generate_jti()},
          bearer
        )

      refute newer.id == first.id
    end
  end

  test "development binding references match the approved immutable packet and bytes" do
    packet =
      "docs/delivery/content-evidence/content_media/verification_messages/VERIFICATION_MESSAGE_EVIDENCE_PACKET_v0.2.0.json"
      |> File.read!()
      |> Jason.decode!()

    for locale <- ["en", "af"] do
      input = attrs(locale)
      version = Enum.find(packet["locale_versions"], &(&1["locale"] == locale))
      assert packet["content_item"]["id"] == input.content_item_id
      assert packet["content_version"]["id"] == input.content_version_id
      assert version["id"] == input.translation_version_id
      assert version["sha256"] == input.content_sha256
      assert version["development_fixture_status"] == "development_approved"

      digest =
        version["artifact_path"]
        |> File.read!()
        |> then(&:crypto.hash(:sha256, &1))
        |> Base.encode16(case: :lower)

      assert digest == input.content_sha256
    end
  end

  test "platform name is frozen and conflicting destination does not overwrite it" do
    input = attrs()
    bearer = :crypto.strong_rand_bytes(32)
    original = NewYou.platform_name()
    on_exit(fn -> Application.put_env(:new_you, :platform_name, original) end)
    {:ok, first} = Communications.establish_verification(input, bearer)
    Application.put_env(:new_you, :platform_name, "Renamed")
    {:ok, replay} = Communications.establish_verification(input, bearer)
    assert replay.platform_name == original
    assert replay.id == first.id

    assert {:error, _} =
             Communications.establish_verification(
               %{input | destination: "other@example.test"},
               bearer
             )
  end

  test "rejects bearer-shaped source references" do
    input = %{attrs() | source_reference: "header.payload.signature"}

    assert {:error, _} =
             Communications.establish_verification(input, :crypto.strong_rand_bytes(32))
  end

  test "rejects unbounded destination provenance" do
    input = %{attrs() | destination_provenance: "unexpected bearer-shaped metadata"}

    assert {:error, _} =
             Communications.establish_verification(input, :crypto.strong_rand_bytes(32))
  end

  test "failure returns a bounded error and does not log the bearer" do
    input = attrs()
    bearer = Base.url_encode64(:crypto.strong_rand_bytes(32), padding: false)
    Application.delete_env(:new_you, :communications_keyring)

    log =
      ExUnit.CaptureLog.capture_log(fn ->
        result = Communications.establish_verification(input, bearer)
        assert result == {:error, :verification_obligation_unavailable}
      end)

    leaked = String.contains?(log, bearer)
    refute leaked
  end

  test "missing key rolls back intent and ciphertext is stored without plaintext" do
    input = attrs()
    bearer = :crypto.strong_rand_bytes(32)
    keyring = Application.fetch_env!(:new_you, :communications_keyring)
    Application.delete_env(:new_you, :communications_keyring)
    assert {:error, _} = Communications.establish_verification(input, bearer)

    {:ok, %{rows: [[count]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT count(*) FROM message_intents WHERE source_reference = $1",
        [input.source_reference]
      )

    assert count == 0
    Application.put_env(:new_you, :communications_keyring, keyring)
    {:ok, intent} = Communications.establish_verification(input, bearer)
    inspected = inspect(intent)

    no_bearer =
      :binary.match(inspected, bearer) == :nomatch and
        not String.contains?(inspected, Base.encode64(bearer))

    assert no_bearer
    refute String.contains?(inspected, input.destination)

    {:ok, %{rows: [[ciphertext, nonce, tag]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT ciphertext, nonce, tag FROM communications_protected_envelopes WHERE message_intent_id = $1",
        [Ecto.UUID.dump!(intent.id)]
      )

    different = ciphertext != bearer
    assert different
    assert byte_size(nonce) == 12
    assert byte_size(tag) == 16

    valid =
      NewYou.Communications.EnvelopeCrypto.decrypt_versioned(
        keyring.keys,
        "test",
        {intent.id, input.source_reference, "email_verification"},
        %{ciphertext: ciphertext, nonce: nonce, tag: tag}
      ) == {:ok, bearer}

    assert valid

    duplicate_attrs = %{
      message_intent_id: intent.id,
      source_reference: input.source_reference,
      purpose: "email_verification",
      key_version: "test",
      nonce: :crypto.strong_rand_bytes(12),
      ciphertext: :crypto.strong_rand_bytes(32),
      tag: :crypto.strong_rand_bytes(16)
    }

    duplicate =
      Ash.create(NewYou.Communications.ProtectedEnvelope, duplicate_attrs,
        action: :store,
        domain: Communications,
        authorize?: false
      )

    assert match?({:error, _}, duplicate)

    {:ok, %{rows: [[stored]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT ciphertext FROM communications_protected_envelopes WHERE message_intent_id = $1",
        [Ecto.UUID.dump!(intent.id)]
      )

    unchanged = stored == ciphertext
    assert unchanged
  end

  test "ordinary authorized reads cannot expose the intent" do
    {:ok, _} = Communications.establish_verification(attrs(), :crypto.strong_rand_bytes(32))

    assert {:ok, []} =
             Ash.read(NewYou.Communications.MessageIntent,
               domain: Communications,
               authorize?: true
             )
  end

  test "a nonce remains reserved after its envelope is removed" do
    {:ok, intent} = Communications.establish_verification(attrs(), :crypto.strong_rand_bytes(32))
    id = Ecto.UUID.dump!(intent.id)

    {:ok, %{rows: [[nonce]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT nonce FROM communications_protected_envelopes WHERE message_intent_id = $1",
        [id]
      )

    {1, _} =
      Repo.delete_all(
        from e in "communications_protected_envelopes", where: e.message_intent_id == ^id
      )

    result =
      Ash.create(NewYou.Communications.EnvelopeNonce, %{nonce: nonce},
        action: :reserve,
        domain: Communications,
        authorize?: false
      )

    assert match?({:error, _}, result)
  end

  test "outer source transaction rollback removes both intent and envelope" do
    input = attrs()
    bearer = :crypto.strong_rand_bytes(32)

    result =
      Ash.transact(
        [NewYou.Communications.MessageIntent, NewYou.Communications.ProtectedEnvelope],
        fn ->
          {:ok, _} = Communications.establish_verification(input, bearer)
          {:error, :source_rejected}
        end
      )

    assert match?({:error, _}, result)

    {:ok, %{rows: [[count]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT count(*) FROM message_intents WHERE source_reference = $1",
        [input.source_reference]
      )

    assert count == 0

    {:ok, %{rows: [[count]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT count(*) FROM communications_protected_envelopes WHERE source_reference = $1",
        [input.source_reference]
      )

    assert count == 0
  end

  test "an envelope persistence failure rolls back its intent and nonce reservation" do
    input = attrs()

    Application.put_env(:new_you, :communications_keyring, %{
      active: "",
      keys: %{"" => :crypto.strong_rand_bytes(32)}
    })

    {:ok, %{rows: [[before_count]]}} =
      Ecto.Adapters.SQL.query(Repo, "SELECT count(*) FROM communications_envelope_nonces", [])

    assert {:error, :verification_obligation_unavailable} =
             Communications.establish_verification(input, :crypto.strong_rand_bytes(32))

    {:ok, %{rows: [[intent_count]]}} =
      Ecto.Adapters.SQL.query(
        Repo,
        "SELECT count(*) FROM message_intents WHERE source_reference = $1",
        [input.source_reference]
      )

    {:ok, %{rows: [[after_count]]}} =
      Ecto.Adapters.SQL.query(Repo, "SELECT count(*) FROM communications_envelope_nonces", [])

    assert intent_count == 0
    assert after_count == before_count
  end

  test "the database admits only the four governed dispatch dispositions" do
    {:ok, intent} = Communications.establish_verification(attrs(), :crypto.strong_rand_bytes(32))
    id = Ecto.UUID.dump!(intent.id)

    {:error, :finished} =
      Repo.transaction(
        fn ->
          for state <- ["open", "held", "reconciliation_required", "closed"] do
            assert {:ok, _} =
                     Ecto.Adapters.SQL.query(
                       Repo,
                       "UPDATE message_intents SET dispatch_disposition = $1 WHERE id = $2",
                       [state, id]
                     )
          end

          assert {:error, _} =
                   Ecto.Adapters.SQL.query(
                     Repo,
                     "UPDATE message_intents SET dispatch_disposition = $1 WHERE id = $2",
                     ["queued", id]
                   )

          Repo.rollback(:finished)
        end,
        mode: :savepoint
      )
  end
end
