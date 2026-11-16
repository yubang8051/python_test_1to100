"""Sum the integers from 1 through 100, inclusive."""


def sum_one_to_hundred() -> int:
    """Print each running total and return the sum from 1 through 100."""
    total = 0
    for number in range(1, 101):
        total += number
        print(f"After adding {number}: {total}")
    return total


if __name__ == "__main__":
    print(sum_one_to_hundred())
