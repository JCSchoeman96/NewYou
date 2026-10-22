defmodule NewYou.LocalConfigTest do
  use ExUnit.Case, async: true

  alias NewYou.LocalConfig

  defp environment(overrides \\ %{}) do
    values =
      Map.merge(
        %{
          "DEV_DATABASE_HOST" => "127.0.0.1",
          "DEV_DATABASE_PORT" => "55432",
          "DEV_DATABASE_USERNAME" => "new_you_dev",
          "DEV_DATABASE_NAME" => "new_you_dev",
          "DEV_DATABASE_PASSWORD" => "dev-test-placeholder",
          "TEST_DATABASE_HOST" => "127.0.0.1",
          "TEST_DATABASE_PORT" => "55433",
          "TEST_DATABASE_USERNAME" => "new_you_test",
          "TEST_DATABASE_NAME" => "new_you_test",
          "TEST_DATABASE_PASSWORD" => "test-placeholder"
        },
        overrides
      )

    &Map.get(values, &1)
  end

  test "DEV and TEST have distinct deterministic database targets" do
    dev = LocalConfig.repo(:dev, environment())
    test = LocalConfig.repo(:test, environment())

    assert {dev[:hostname], dev[:port], dev[:username], dev[:database]} ==
             {"127.0.0.1", 55432, "new_you_dev", "new_you_dev"}

    assert {test[:hostname], test[:port], test[:username], test[:database]} ==
             {"127.0.0.1", 55433, "new_you_test", "new_you_test"}

    refute test[:password] == dev[:password]
  end

  test "TEST rejects DEV endpoint, role, or database even when credentials exist" do
    for {key, value} <- [
          {"TEST_DATABASE_PORT", "55432"},
          {"TEST_DATABASE_HOST", "localhost"},
          {"TEST_DATABASE_USERNAME", "new_you_dev"},
          {"TEST_DATABASE_NAME", "new_you_dev"}
        ] do
      assert_raise ArgumentError, ~r/DevCore contract/, fn ->
        LocalConfig.repo(:test, environment(%{key => value}))
      end
    end
  end

  test "missing TEST credentials never fall back to DEV or DATABASE_URL" do
    env =
      environment(%{
        "TEST_DATABASE_PASSWORD" => nil,
        "DATABASE_URL" => "ecto://new_you_dev:placeholder@127.0.0.1:55432/new_you_dev"
      })

    assert_raise ArgumentError, ~r/TEST_DATABASE_PASSWORD.*devcore-project/, fn ->
      LocalConfig.repo(:test, env)
    end
  end

  test "empty credentials and test partitions fail closed" do
    assert_raise ArgumentError, fn ->
      LocalConfig.repo(:test, environment(%{"TEST_DATABASE_PASSWORD" => ""}))
    end

    assert_raise ArgumentError, ~r/MIX_TEST_PARTITION/, fn ->
      LocalConfig.repo(:test, environment(%{"MIX_TEST_PARTITION" => "1"}))
    end
  end

  test "primary checkout uses only 4220" do
    assert LocalConfig.port(false, nil) == 4220
    assert LocalConfig.port(false, "4220") == 4220
    assert_raise ArgumentError, fn -> LocalConfig.port(false, "4221") end
  end

  test "worktree requires an explicit port in 4221 through 4239" do
    for port <- 4221..4239 do
      assert LocalConfig.port(true, Integer.to_string(port)) == port
    end

    for port <- [nil, "", "4220", "4240", "4221oops"] do
      assert_raise ArgumentError, fn -> LocalConfig.port(true, port) end
    end
  end
end
