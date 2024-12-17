import unittest
from two_pointers_extra import cnt_seqs as func


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(func([4, 2, 1], 3, 2), 2)
        print('test_one passed')

    def test_two(self):
        self.assertEqual(func([3, 8, 5, 7, 1, 2, 4, 9, 6], 9, 2), 3)
        print('test_two passed')

    def test_three(self):
        self.assertEqual(func([1, 3, 1], 3, 2), 3)
        print('test_three passed')

    def test_four(self):
        self.assertEqual(func([32, 77, 1, 100], 4, 4), 1)
        print('test_four passed')

    def test_five(self):
        self.assertEqual(func([1, 3, 1], 3, 0), 2)
        print('test_five passed')
    
    def test_same_at_the_end(self):
        self.assertEqual(func([1, 2, 3, 4, 5, 5, 5], 7, 1), 4) 
        print('test_same_at_the_end passed')

    def test_same_at_the_end_2(self):
        self.assertEqual(func([1, 2, 3, 4, 4, 4], 6, 1), 4)
        print('test_same_at_the_end_2 passed')

    def test_same_at_the_end_3(self):
        self.assertEqual(func([1, 2, 3, 4, 4, 4, 5, 5, 5],9, 1), 6)
        print('test_same_at_the_end_3 passed')

    def test_big_diff(self):
        self.assertEqual(func([x for x in range(100000)], 99999, 0), 1)
        print('test_big_diff passed')

    def test_wrong(self):
        self.assertNotEqual(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 2), 10)
        print('test_wrong passed')


if __name__ == '__main__':
    unittest.main()