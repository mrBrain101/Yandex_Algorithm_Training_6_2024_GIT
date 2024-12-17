import unittest
from sum_nums_with_prefix_sum import cntsumofk as func

class Testfunc(unittest.TestCase):
    def test_small_input(self):
        nums = [1, 2, 3]
        k = 3
        self.assertEqual(func(nums, k), 2)

    def test_k_is_one(self):
        nums = [1, 2, 3]
        k = 1
        self.assertEqual(func(nums, k), 1)

    def test_k_is_large(self):
        nums = [1, 2, 3]
        k = 1000000000
        self.assertEqual(func(nums, k), 0)

    def test_k_is_zero(self):
        nums = [1, 2, 3]
        k = 0
        self.assertEqual(func(nums, k), 0)

    def test_k_is_negative(self):
        nums = [0, -1, 2]
        k = -1
        self.assertEqual(func(nums, k), 2)

    def test_empty_input(self):
        nums = []
        k = 2
        self.assertEqual(func(nums, k), 0)

    def test_single_element_input(self):
        nums = [5]
        k = 2
        self.assertEqual(func(nums, k), 0)

if __name__ == '__main__':
    unittest.main()