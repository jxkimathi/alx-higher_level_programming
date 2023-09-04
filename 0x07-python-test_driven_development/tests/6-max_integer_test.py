#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest to find and return the max num"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4], 4))
        self.assertEqual(max_integer([1, 3, 4, 2], 4))
        self.assertEqual(max_integer([4, 3, 2, 1], 4))
        self.assertEqual(max_integer([-1, -2, -3, -4], -1))
        self.assertEqual(max_integer([1], 1))
        self.assertEqual(max_integer([], None))
        self.assertEqual(max_integer([4.32, 5.48, 4.23, 2.34], 5.48))
        self.assertEqual(max_integer([4.32, -2, 2.34, -4], 4.32))
        

    if __name__ == '__main__':
        unittest.main()
