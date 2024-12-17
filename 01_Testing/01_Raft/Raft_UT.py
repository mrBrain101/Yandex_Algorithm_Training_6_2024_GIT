from Raft import find_direction_to_closest_point
import unittest

class YAlgo_Raft_01_UT(unittest.TestCase):
    def test_NW(self):
        self.assertEqual(find_direction_to_closest_point('-1 -2 5 3 -4 6'), 'NW')

    def test_NE(self):
        self.assertEqual(find_direction_to_closest_point('-99 -99 99 99 100 100'), 'SE')
        self.assertEqual(find_direction_to_closest_point('0 0 10 10 20 20'), 'SE')
        self.assertEqual(find_direction_to_closest_point('-10 -10 0 0 20 20'), 'SE')

if __name__ == '__main__':
    unittest.main()