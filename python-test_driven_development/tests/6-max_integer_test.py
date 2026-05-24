#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function."""

    def test_regular_list(self):
        """Test with a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_negative_positive(self):
        """Test with mixed negative and positive numbers."""
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_identical_elements(self):
        """Test with all identical elements."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test with mixed int and float values."""
        self.assertEqual(max_integer([1, 2.9, 2]), 2.9)

    def test_no_argument(self):
        """Test with no argument (default empty list)."""
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()
