import unittest
from prefix_sum import makeprefixsum
class TestMakePrefixSum(unittest.TestCase):
    def test_empty_list(self):
        nums = []
        expected = []
        self.assertEqual(makeprefixsum(nums), expected)

    def test_single_element_list(self):
        nums = [1]
        expected = [1]
        self.assertEqual(makeprefixsum(nums), expected)

    def test_multiple_elements_list(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 3, 6, 10, 15]
        self.assertEqual(makeprefixsum(nums), expected)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        expected = [-1, -3, -6, -10, -15]
        self.assertEqual(makeprefixsum(nums), expected)

    def test_mixed_numbers(self):
        nums = [1, -2, 3, -4, 5]
        expected = [1, -1, 2, -2, 3]
        self.assertEqual(makeprefixsum(nums), expected)
    
    def test_zero_first_element(self):
        nums = [0, 1, 2, 3, 4]
        expected = [0, 1, 3, 6, 10]
        self.assertEqual(makeprefixsum(nums), expected)

    def test_large_list(self):
        nums = [i for i in range(1000)]
        expected = [i*(i+1)//2 for i in range(1000)]
        self.assertEqual(makeprefixsum(nums), expected)

if __name__ == '__main__':
    unittest.main()