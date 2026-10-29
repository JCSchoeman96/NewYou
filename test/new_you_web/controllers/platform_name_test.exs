defmodule NewYouWeb.PlatformNameTest do
  use NewYouWeb.ConnCase, async: false

  test "production runtime rejects a missing or development platform name" do
    original = System.get_env("PLATFORM_NAME")

    on_exit(fn ->
      if original,
        do: System.put_env("PLATFORM_NAME", original),
        else: System.delete_env("PLATFORM_NAME")
    end)

    for value <- [nil, "", "  ", "Development Platform", " Test Platform "] do
      if value,
        do: System.put_env("PLATFORM_NAME", value),
        else: System.delete_env("PLATFORM_NAME")

      assert_raise RuntimeError, ~r/PLATFORM_NAME/, fn ->
        Config.Reader.read!("config/runtime.exs", env: :prod)
      end
    end
  end

  test "the test environment has an explicit non-production name" do
    assert NewYou.platform_name() == "Test Platform"
    assert Application.spec(:new_you, :modules) |> Enum.member?(NewYou)
  end

  test "the page title uses the configured platform name", %{conn: conn} do
    original = Application.fetch_env!(:new_you, :platform_name)
    on_exit(fn -> Application.put_env(:new_you, :platform_name, original) end)
    Application.put_env(:new_you, :platform_name, "Example Public Name")

    assert html_response(get(conn, ~p"/"), 200) =~ ">Example Public Name</title>"
  end
end
