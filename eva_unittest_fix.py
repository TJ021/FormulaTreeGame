import unittest
from formula_game_functions import *


class EvaluateTests(unittest.TestCase):

    def test_leaf1(self):
        b = Leaf('x')
        a = evaluate(b, 'x', '1')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_leaf2(self):
        b = Leaf('x')
        a = evaluate(b, 'x', '0')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_not(self):
        b = NotTree(Leaf('x'))
        a = evaluate(b, 'x', '0')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_not2(self):
        b = NotTree(Leaf('x'))
        a = evaluate(b, 'x', '1')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_or(self):
        b = OrTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '11')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_or2(self):
        b = OrTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '01')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_or3(self):
        b = OrTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '10')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_or4(self):
        b = OrTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '00')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and(self):
        b = AndTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '00')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and2(self):
        b = AndTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '01')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and3(self):
        b = AndTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '10')
        self.assertEqual(a, 0, 'Should equal 0')

    def test_and4(self):
        b = AndTree(Leaf('x'), Leaf('y'))
        a = evaluate(b, 'xy', '11')
        self.assertEqual(a, 1, 'Should equal 1')

    def test_combination(self):
        b = NotTree(OrTree(OrTree(Leaf('z'), AndTree(AndTree(AndTree(OrTree(
            Leaf('z'), OrTree(Leaf('y'), AndTree(Leaf('z'), Leaf('z')))),
            Leaf('y')), OrTree(AndTree(OrTree(Leaf('y'), NotTree(Leaf('z'))),
                                       Leaf('z')), Leaf('x'))), AndTree(
            Leaf('x'), Leaf('x')))), NotTree(Leaf('y'))))
        a = evaluate(b, 'xyz', '010')
        self.assertEqual(a, 1, 'Should be 1')

    def test_combinations2(self):
        b = OrTree(AndTree(NotTree(OrTree(Leaf('y'), Leaf('z'))), Leaf('z')),
                   AndTree(NotTree(AndTree(AndTree(Leaf('x'),
                                                   NotTree(Leaf('x'))),
        NotTree(AndTree(Leaf('x'), AndTree(Leaf('z'), NotTree(Leaf('y'))))))),
                           AndTree(Leaf('y'), OrTree(Leaf('x'), Leaf('y')))))
        a = evaluate(b,'xyz', '101')
        self.assertEqual(a, 0, 'Should be 0')

if __name__ == "__main__":
    unittest.main()
