import unittest
from formula_game_functions import *


class EvaluateTests(unittest.TestCase):

    def test_OneMoveMissingE(self):
        a = build_tree('x')
        result = play2win(a, 'EA', 'x', '')
        self.assertEqual(result, 1, 'Should equal 1')

    def test_OneMoveMissingA(self):
        a = build_tree('x')
        result = play2win(a, 'AA', 'x', '')
        self.assertEqual(result, 0, 'Should equal 0')

    def test_OneMoveMissingE_NotTree(self):
        a = build_tree('-x')
        result = play2win(a, 'EA', 'x', '')
        self.assertEqual(result, 0, 'Should equal 0')

    def test_OneMoveMissingA_NotTree(self):
        a = build_tree('-x')
        result = play2win(a, 'AA', 'xy', '')
        self.assertEqual(result, 1, 'Should equal 1')

    def test_OneMoveMissingE_OrTree(self):
        a = build_tree('(x+y)')
        result = play2win(a, 'AE', 'xy', '1')
        self.assertEqual(result, 1, 'Should equal 1')

    def test_OneMoveMissingA_OrTree(self):
        a = build_tree('(x+y)')
        result = play2win(a, 'AA', 'xy', '1')
        self.assertEqual(result, 0, 'Should equal 0')

    def test_OneMoveMissingE_AndTree(self):
        a = build_tree('(x*y)')
        result = play2win(a, 'EE', 'xy', '1')
        self.assertEqual(result, 1, 'Should equal 1')

    def test_OneMoveMissingA_AndTree(self):
        a = build_tree('(x*y)')
        result = play2win(a, 'AA', 'xy', '1')
        self.assertEqual(result, 0, 'Should equal 0')

    def test_MultipleMovesMissingE_AndTree(self):
        a = build_tree('(x*y)')
        result = play2win(a, 'EA', 'xy', '')
        self.assertEqual(result, 1, 'Should equal 1')

    def test_MultipleMovesMissingA_AndTree(self):
        a = build_tree('(x*y)')
        result = play2win(a, 'AE', 'xy', '')
        self.assertEqual(result, 0, 'Should equal 0')

    def test_final(self):
        formula = '((-a+b)*-(c+d))'
        root = build_tree(formula)
        first = play2win(root, 'EEEE', 'abcd', '')
        second = play2win(root, 'EEEE', 'abcd', str(first))
        third = play2win(root, 'EEEE', 'abcd', str(first) + str(second))
        forth = play2win(root, 'EEEE', 'abcd',
                         str(first) + str(second) + str(third))
        result = str(first) + str(second) + str(third) + str(forth)
        self.assertEqual(result, '1100', 'It should be 1100')

if __name__ == "__main__":
    unittest.main()
