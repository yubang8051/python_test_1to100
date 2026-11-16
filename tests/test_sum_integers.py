"""Tests for the integer summation function."""

import io
from pathlib import Path
import subprocess
import sys
import unittest
from contextlib import redirect_stdout

from src.sum_integers import sum_one_to_hundred, sum_one_to_n


class SumIntegersTests(unittest.TestCase):
    def test_requested_upper_bounds(self):
        for n, expected in [(0, 0), (1, 1), (10, 55), (100, 5050),
                            (1000, 500500)]:
            with self.subTest(n=n):
                output = io.StringIO()
                with redirect_stdout(output):
                    self.assertEqual(sum_one_to_n(n), expected)
                self.assertEqual(len(output.getvalue().splitlines()), n)

    def test_function_rejects_negative_and_non_integer_inputs(self):
        for value, error in [(-1, ValueError), (1.5, TypeError),
                             ("10", TypeError), (True, TypeError)]:
            with self.subTest(value=value), self.assertRaises(error):
                sum_one_to_n(value)

    def run_cli(self, *args):
        script = Path(__file__).resolve().parents[1] / "src" / "sum_integers.py"
        return subprocess.run([sys.executable, str(script), *args],
                              capture_output=True, text=True, check=False)

    def test_cli_requested_upper_bounds(self):
        for n in (0, 1, 10, 100, 1000):
            with self.subTest(n=n):
                result = self.run_cli(str(n))
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stderr, "")
                expected_lines = [
                    f"After adding {i}: {i * (i + 1) // 2}"
                    for i in range(1, n + 1)
                ] + [str(n * (n + 1) // 2)]
                self.assertEqual(result.stdout.splitlines(), expected_lines)

    def test_cli_rejects_invalid_inputs(self):
        for value in ("-1", "1.5", "abc", ""):
            with self.subTest(value=value):
                result = self.run_cli(value)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)

    def test_cli_default_preserves_original_output(self):
        self.assertEqual(self.run_cli().stdout, self.run_cli("100").stdout)
        self.assertEqual(self.run_cli().returncode, 0)

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
