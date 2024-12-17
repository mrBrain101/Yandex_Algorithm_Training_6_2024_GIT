import unittest
from two_pointers import cntpairs

class TestCntPairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(cntpairs([], 0, 1), 0)

    def test_single_element_list(self):
        self.assertEqual(cntpairs([1], 1, 1), 0)

    def test_no_pairs(self):
        self.assertEqual(cntpairs([1, 2, 3], 3, 1), 1)

    def test_all_pairs(self):
        self.assertEqual(cntpairs([1, 1, 1], 3, 1), 0)

    def test_example_from_che_city(self):
        self.assertEqual(cntpairs([1, 3, 5, 8], 4, 4), 2)

    def test_negative_numbers(self):
        self.assertEqual(cntpairs([-3, 1, 5, 8], 4, 4), 3)

if __name__ == '__main__':
    unittest.main()