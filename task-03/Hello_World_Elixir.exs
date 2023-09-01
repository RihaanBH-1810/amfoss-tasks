defmodule PrimeNumbers do
  def check_if_prime(2), do: true
  def check_if_prime(number) when number <= 1 or rem(number, 2) == 0, do: false
  def check_if_prime(number), do: not Enum.any?(2..round(:math.sqrt(number)), fn x -> rem(number, x) == 0 end)

  def prime_numbers(number) when number < 2, do: []
  def prime_numbers(number) do
    Enum.filter(2..number, &check_if_prime/1)
  end

  def main do
    input = IO.gets("") |> String.trim() |> String.to_integer()

    case input do
      number when number >= 2 ->
        primes = prime_numbers(number)
        if Enum.empty?(primes) do
          IO.puts("There are no prime numbers up to #{number}.")
        else
          IO.puts(Enum.join(primes, " "))
        end
      _ ->
        IO.puts("Wrong input")
    end
  end
end

PrimeNumbers.main()
