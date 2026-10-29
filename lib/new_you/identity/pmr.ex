defmodule NewYou.Identity.PMR do
  @moduledoc false

  @data_alphabet "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  @check_alphabet @data_alphabet <> "*"
  @known_data_prefix "PMR"

  @spec check(term()) :: String.t() | nil
  def check("PMR" <> data) when byte_size(data) == 16 do
    if valid_data?(data) do
      remainder =
        for <<character <- @known_data_prefix <> data>>, reduce: 0 do
          remainder ->
            rem((remainder + value(character)) * 2, 37)
        end

      check_value = rem(38 - remainder, 37)
      "PMR-" <> data <> binary_part(@check_alphabet, check_value, 1)
    end
  end

  def check(_), do: nil

  @spec valid?(term()) :: boolean()
  def valid?("PMR-" <> <<data::binary-size(16), check_character>>) do
    valid_data?(data) and check("PMR" <> data) == "PMR-" <> data <> <<check_character>>
  end

  def valid?(_), do: false

  @spec generate() :: {:ok, String.t()} | {:error, :generation_failed}
  def generate do
    data =
      for _ <- 1..16, into: <<>> do
        index = :crypto.strong_rand_range(36)
        binary_part(@data_alphabet, index, 1)
      end

    case check("PMR" <> data) do
      pmr when is_binary(pmr) -> {:ok, pmr}
      _ -> {:error, :generation_failed}
    end
  rescue
    _ -> {:error, :generation_failed}
  end

  defp valid_data?(data) do
    byte_size(data) == 16 and
      Enum.all?(:binary.bin_to_list(data), &(&1 in String.to_charlist(@data_alphabet)))
  end

  defp value(byte) when byte in ?0..?9, do: byte - ?0
  defp value(byte) when byte in ?A..?Z, do: byte - ?A + 10
  defp value(?*), do: 36
end
