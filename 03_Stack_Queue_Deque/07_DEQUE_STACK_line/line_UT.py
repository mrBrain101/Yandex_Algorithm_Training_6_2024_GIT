import unittest
from line import time_line as func

class TestLine(unittest.TestCase):
    def test_line1(self):
        self.assertEqual(func(3, 4, [1, 5, 9]), 22)

    def test_line2(self):
        self.assertEqual(func(5, 5, [0, 0, 0, 0, 0]), 0)

    def test_line3(self):
        self.assertEqual(func(5, 5, [1, 2, 3, 4, 5]), 15)

    def test_line4(self):
        self.assertEqual(func(5, 5, [0, 0, 0, 0, 10]), 15)

    def test_line5(self):
        self.assertEqual(func(6, 2, [1, 0, 1, 0, 1, 0]), 3)

    def test_line6(self):
        self.assertEqual(func(3, 3, [10, 0, 0]), 22)

if __name__ == '__main__':
    unittest.main()