import unittest

class TestMathsWorks(unittest.TestCase):

    def test_addition(self):
        expected = 8
        actual = 4 + 4
        self.assertEqual(expected, actual)

    def test_multiplication(self):
        expected = 10
        actual = 5 * 2
        self.assertEqual(expected, actual)

    def test_small_numbers_are_less_than_big_ones(self):
        small = 0.0031
        big = 934193432987
        self.assertTrue(small < big)

    def test_that_division_by_zero_does_not_work(self):
        with self.assertRaises(ZeroDivisionError):
            actual = 3/0

if __name__ == '__main__':
    unittest.main()
