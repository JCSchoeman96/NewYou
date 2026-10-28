defmodule NewYou.Identity.Email do
  @moduledoc false

  @atext String.to_charlist("!#$%&'*+-/=?^_`{|}~")

  @spec canonicalize(term()) :: {:ok, String.t()} | {:error, :invalid_email}
  def canonicalize(email) when is_binary(email) do
    email = trim_ascii_space_and_tab(email)

    with true <- byte_size(email) <= 254,
         [local_part, domain] <- :binary.split(email, "@", [:global]),
         true <- valid_local_part?(local_part),
         true <- valid_domain?(domain),
         canonical_domain <- ascii_downcase(domain),
         canonical <- local_part <> "@" <> canonical_domain,
         true <- byte_size(canonical) <= 254 do
      {:ok, canonical}
    else
      _ -> {:error, :invalid_email}
    end
  end

  def canonicalize(_), do: {:error, :invalid_email}

  defp valid_local_part?(local_part) do
    atoms = String.split(local_part, ".", trim: false)

    byte_size(local_part) in 1..64 and
      Enum.all?(atoms, fn atom ->
        atom != "" and Enum.all?(:binary.bin_to_list(atom), &atext?/1)
      end)
  end

  defp atext?(byte) when byte in ?A..?Z, do: true
  defp atext?(byte) when byte in ?a..?z, do: true
  defp atext?(byte) when byte in ?0..?9, do: true
  defp atext?(byte), do: byte in @atext

  defp valid_domain?(domain) do
    labels = String.split(domain, ".", trim: false)

    byte_size(domain) in 1..253 and
      String.valid?(domain) and
      String.match?(domain, ~r/\A[\x00-\x7F]+\z/) and
      length(labels) >= 2 and Enum.all?(labels, &valid_domain_label?/1)
  end

  defp valid_domain_label?(label) do
    byte_size(label) in 1..63 and
      not String.starts_with?(ascii_downcase(label), "xn--") and
      String.match?(label, ~r/\A[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\z/)
  end

  defp ascii_downcase(value) do
    for <<byte <- value>>, into: <<>> do
      if byte in ?A..?Z, do: <<byte + 32>>, else: <<byte>>
    end
  end

  defp trim_ascii_space_and_tab(value) do
    value
    |> trim_left_ascii_space_and_tab()
    |> trim_right_ascii_space_and_tab()
  end

  defp trim_left_ascii_space_and_tab(<<byte, rest::binary>>) when byte in [32, 9],
    do: trim_left_ascii_space_and_tab(rest)

  defp trim_left_ascii_space_and_tab(value), do: value

  defp trim_right_ascii_space_and_tab(<<>>), do: <<>>

  defp trim_right_ascii_space_and_tab(value) do
    last = :binary.last(value)

    if last in [32, 9] do
      trim_right_ascii_space_and_tab(binary_part(value, 0, byte_size(value) - 1))
    else
      value
    end
  end
end
