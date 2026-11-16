"""Tests for the integer summation function."""

import io
import unittest
from contextlib import redirect_stdout

from src.sum_integers import sum_one_to_hundred


class SumIntegersTests(unittest.TestCase):
    def test_sum_one_through_one_hundred_is_5050(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = sum_one_to_hundred()

        self.assertEqual(result, 5050)
        lines = output.getvalue().splitlines()
        expected_total = 0
        self.assertEqual(len(lines), 100)
        for number, line in enumerate(lines, start=1):
            expected_total += number
            self.assertEqual(line, f"After adding {number}: {expected_total}")


if __name__ == "__main__":
    unittest.main()
