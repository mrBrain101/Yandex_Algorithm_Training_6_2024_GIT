import unittest
from del_median import del_median as func

class TestDelMedian(unittest.TestCase):
    def test_example1(self):
        nums = [19, 3, 8]
        n = 3
        result = func(nums, n)
        self.assertEqual(result, [8, 3, 19])

    def test_example2(self):
        nums = [1, 2, 4, 2]
        n = 4
        result = func(nums, n)
        self.assertEqual(result, [2, 2, 1, 4])

    def test_single_element(self):
        nums = [5]
        n = 1
        result = func(nums, n)
        self.assertEqual(result, [5])

    def test_even_length(self):
        nums = [3, 1, 5, 7]
        n = 4
        result = func(nums, n)
        self.assertEqual(result, [3, 5, 1, 7])

    def test_odd_length(self):
        nums = [1, 3, 5, 7, 9]
        n = 5
        result = func(nums, n)
        self.assertEqual(result, [5, 3, 7, 1, 9])

    def test_duplicate_elements(self):
        nums = [1, 1, 3, 3, 5, 5]
        n = 6
        result = func(nums, n)
        self.assertEqual(result, [3, 3, 1, 5, 1, 5])

if __name__ == '__main__':
    unittest.main()