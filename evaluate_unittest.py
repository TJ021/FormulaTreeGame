import unittest
from formula_game_functions import *


class EvaluateTests(unittest.TestCase):

    def test_leaf1(self):
        a = evaluate(build_tree('x'), 'x', '1')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_leaf2(self):
        a = evaluate(build_tree('x'), 'x', '0')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_not(self):
        a = evaluate(build_tree('-x'), 'x', '0')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_not2(self):
        a = evaluate(build_tree('-x'), 'x', '1')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_or(self):
        a = evaluate(build_tree('(x+y)'), 'xy', '11')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_or2(self):
        a = evaluate(build_tree('(x+y)'), 'xy', '01')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_or3(self):
        a = evaluate(build_tree('(x+y)'), 'xy', '10')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_or4(self):
        a = evaluate(build_tree('(x+y)'), 'xy', '00')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and(self):
        a = evaluate(build_tree('(x*y)'), 'xy', '00')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and2(self):
        a = evaluate(build_tree('(x*y)'), 'xy', '01')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and3(self):
        a = evaluate(build_tree('(x*y)'), 'xy', '10')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and4(self):
        a = evaluate(build_tree('(x*y)'), 'xy', '11')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_combination(self):
        a = evaluate(build_tree('-((z+((((z+(y+(z*z)))*y)*(((y+-z)'
                                '*z)+x))*(x*x)))+-y)'), 'xyz', '010')
        self.assertEqual(a, 1, 'Should be 1')

    def test_combinations2(self):
        a = evaluate(
            build_tree('((-(y+z)*z)+(-((x*-x)*-(x*(z*-y)))*(y*(x+y))))'),
            'xyz', '101')
        self.assertEqual(a, 0, 'Should be 0')

if __name__ == "__main__":
    unittest.main()
