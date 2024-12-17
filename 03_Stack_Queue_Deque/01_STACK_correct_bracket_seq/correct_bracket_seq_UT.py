import unittest
from correct_bracket_seq import bracket_stack

class TestCorrectBracketSeq(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bracket_stack('([]{})'), 'yes')

    def test_2(self):
        self.assertEqual(bracket_stack('()[]{}}'), 'no')

    def test_3(self):
        self.assertEqual(bracket_stack('(]'), 'no')

    def test_4(self):
        self.assertEqual(bracket_stack('()()()()()()()()()()()()()()()()'), 'yes')

    def test_5(self):
        self.assertEqual(bracket_stack('(()()()[][][][][][{}{}{}{()()()()}])'), 'yes')

    def test_6(self):
        self.assertEqual(bracket_stack(''), 'yes')

    def test_7(self):
        self.assertEqual(bracket_stack('([{(()([{}]))}])'), 'yes')

if __name__ == '__main__':
    unittest.main()