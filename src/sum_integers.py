"""Sum integers from 1 through a nonnegative upper bound, defaulting to 100."""

import argparse


def sum_one_to_n(n: int) -> int:
    """Print running totals and return the sum; zero is an empty sum."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("N must be an integer")
    if n < 0:
        raise ValueError("N must be nonnegative")
    total = 0
    for number in range(1, n + 1):
        total += number
        print(f"After adding {number}: {total}")
    return total


def sum_one_to_hundred() -> int:
    """Print each running total and return the sum from 1 through 100."""
    return sum_one_to_n(100)


def nonnegative_integer(value: str) -> int:
    """Validate a CLI upper bound for argparse."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("N must be an integer") from None
    if number < 0:
        raise argparse.ArgumentTypeError("N must be nonnegative")
    return number


def main() -> None:
    """Parse the optional upper bound and print the running and final sums."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", nargs="?", type=nonnegative_integer, default=100,
                        help="nonnegative upper bound (default: 100)")
    args = parser.parse_args()
    print(sum_one_to_n(args.N))


if __name__ == "__main__":
    main()
