"""FizzBuzz: a classic warm-up exercise.

Print numbers 1..n, replacing multiples of 3 with "Fizz",
multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
"""


def fizzbuzz(n):
    """Return the FizzBuzz label for a single number."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def main():
    for n in range(1, 21):
        print(fizzbuzz(n))


if __name__ == "__main__":
    main()
