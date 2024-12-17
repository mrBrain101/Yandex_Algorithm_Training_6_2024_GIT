import unittest
from sum_of_triples import sum_of_triplets as func

class TestSumOfTriples(unittest.TestCase):

    def test_example1(self):
        nums = [10, 6, 10, 3, 7]
        n = 5
        result = func(nums, n)
        self.assertEqual(result, 3346)

    def test_example2(self):
        nums = [1, 2, 3]
        n = 3
        result = func(nums, n)
        self.assertEqual(result, 6)

    def test_example3(self):
        nums = [0, 5, 6, 7]
        n = 4
        result = func(nums, n)
        self.assertEqual(result, 210)

    def test_example4(self):
        nums = [143461, 574468, 902994]
        n = 3
        result = func(nums, n)
        self.assertEqual(result, 630987644)

    def test_example5(self):
        nums = [0, 0, 0]
        n = 3
        result = func(nums, n)
        self.assertEqual(result, 0)

    def test_example6(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        result = func(nums, n)
        self.assertEqual(result, 18150)


if __name__ == '__main__':
    unittest.main()