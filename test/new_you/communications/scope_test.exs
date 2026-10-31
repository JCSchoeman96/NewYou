defmodule NewYou.Communications.ScopeTest do
  use ExUnit.Case, async: true

  test "the slice has no delivery executor or third business resource" do
    assert Enum.sort(Path.wildcard("lib/new_you/communications/**/*.ex")) == [
             "lib/new_you/communications/envelope_crypto.ex",
             "lib/new_you/communications/envelope_nonce.ex",
             "lib/new_you/communications/keyring.ex",
             "lib/new_you/communications/message_intent.ex",
             "lib/new_you/communications/protected_envelope.ex"
           ]

    refute AshOban in Spark.extensions(NewYou.Communications.MessageIntent)
    refute AshOban in Spark.extensions(NewYou.Communications.ProtectedEnvelope)
    refute AshOban in Spark.extensions(NewYou.Communications.EnvelopeNonce)

    assert Enum.sort(
             Enum.map(Ash.Resource.Info.actions(NewYou.Communications.MessageIntent), & &1.name)
           ) == [:establish, :read]
  end
end
