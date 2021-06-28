"""
# Copyright Nick Cheng, Tejasvi Singh, 2016, 2017
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment

# Add your functions here.

# Global variables used to check for operators and to verify if the Leaf's
# symbol is a lower case letter.
operators = '*+'
alpha = 'abcdefghijlkmnopqrstuvwxyz'


def build_tree(formula):
    '''(str) -> FormulaTree or None
    Given a string boolean expression, the function will create and return a
    FormulaTree if the formula is valid, otherwise it will return None.
    >>> build_tree('x')
    Leaf('x')
    >>> build_tree('-x')
    NotTree(Leaf('x'))
    >>> build_tree('(x+y)')
    OrTree(Leaf('x'), Leaf('y'))
    >>> build_tree('X')
    None
    >>> build_tree('x+y')
    None
    >>> build_tree('((x+y)*x)')
    AndTree(OrTree(Leaf('x'), Leaf('y')), Leaf('x'))
    >>> build_tree('((x+y)*(x*y))')
    AndTree(OrTree(Leaf('x'), Leaf('y')), AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree('(x*(x*y))')
    AndTree(Leaf('x'), AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree('(x*-(x*y))')
    AndTree(Leaf('x'), NotTree(AndTree(Leaf('x'), Leaf('y'))))
    >>> build_tree('(-x*(x*y))')
    AndTree(NotTree(Leaf('x')), AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree('(-x*((x*y)*(x+y)))')
    AndTree(NotTree(Leaf('x')), AndTree(AndTree(Leaf('x'), Leaf('y')), \
OrTree(Leaf('x'), Leaf('y'))))
    >>> build_tree('(-x*-((x*y)*(x+y)))')
    AndTree(NotTree(Leaf('x')), NotTree(AndTree(AndTree(Leaf('x'), \
Leaf('y')), OrTree(Leaf('x'), Leaf('y')))))
    '''
    # Checks if the formula is valid.
    valid = validity(formula)

    # If it is valid, another function is called to get the root.
    if valid:
        root = build_tree_helper(formula)

    # If not the root equals None
    else:
        root = None

    # Returns the root.
    return root


def build_tree_helper(formula):
    '''(str) -> FormulaTree
    Given a string boolean expression, the function will create and return a
    FormulaTree.
    REQ: formula must be valid.
    >>> build_tree_helper('x')
    Leaf('x')
    >>> build_tree_helper('-x')
    NotTree(Leaf('x'))
    >>> build_tree_helper('(x+y)')
    OrTree(Leaf('x'), Leaf('y'))
    >>> build_tree_helper('((x+y)*x)')
    AndTree(OrTree(Leaf('x'), Leaf('y')), Leaf('x'))
    >>> build_tree_helper('((x+y)*(x*y))')
    AndTree(OrTree(Leaf('x'), Leaf('y')), AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree_helper('(x*(x*y))')
    AndTree(Leaf('x'), AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree_helper('(x*-(x*y))')
    AndTree(Leaf('x'), NotTree(AndTree(Leaf('x'), Leaf('y'))))
    >>> build_tree_helper('(-x*(x*y))')
    AndTree(NotTree(Leaf('x')), AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree_helper('(-x*((x*y)*(x+y)))')
    AndTree(NotTree(Leaf('x')), AndTree(AndTree(Leaf('x'), Leaf('y')), \
OrTree(Leaf('x'), Leaf('y'))))
    >>> build_tree_helper('(-x*-((x*y)*(x+y)))')
    AndTree(NotTree(Leaf('x')), NotTree(AndTree(AndTree(Leaf('x'), \
Leaf('y')), OrTree(Leaf('x'), Leaf('y')))))
    '''
    # If the length of the formula is 1, then the root equals the Leaf of
    # the formula.
    if len(formula) == 1:
        root = Leaf(formula)

    # If the length is 2, the root equals the NotTree of the Leaf of the
    # formula.
    elif len(formula) == 2:
        root = NotTree(Leaf(formula[1]))

    # If not, the function calls another function that returns the symbol,
    # the left child and the right child.
    else:
        symbol, left_child, right_child = get_symbol_children(formula)

        # Depending on what the symbol is, the root equals its resepctive
        # tree with the parameters being the root of the left child and the
        # root of the right child.
        if symbol == '*':
            root = AndTree(build_tree_helper(left_child),
                           build_tree_helper(right_child))

        elif symbol == '+':
            root = OrTree(build_tree_helper(left_child),
                          build_tree_helper(right_child))

        # If the symbol is '-' the root is the NotTree of the root of the
        # left child.
        elif symbol == '-':
            root = NotTree(build_tree_helper(left_child))

    # returns the root.
    return root


def validity(formula):
    '''(str) -> bool
    Given a string boolean expression, the function will determine if it has
    proper format and return either True or False.
    >>> validity('x')
    True
    >>> validity('X')
    False
    >>> validity('-x')
    True
    >>> validity('-X')
    False
    >>> validity('(x+y)-')
    False
    >>> validity('((x+y)*x)')
    True
    >>> validity('((x+y)-(x*y))')
    False
    >>> validity('(x*(x*y))')
    True
    >>> validity('(x*-(x*y))')
    True
    >>> validity('(-X*(X*Y))')
    False
    >>> validity('(-x*((x*y)*(x+y)))')
    True
    >>> validity('(-x*-((x*y)*(x+y)))')
    True
    '''
    # If the length of the formula is 0, then the formula isn't valid.
    if len(formula) == 0:
        result = False

    # If the length of the formula is 1 and the formula is a lower case
    # character, then the formula is valid, otherwise it's not.
    elif len(formula) == 1:
        if formula in alpha:
            result = True
        else:
            result = False

    # If the length of the formula is 1 and the formula is a dash followed by a
    # lower case character, then the formula is valid, otherwise it's not.
    elif len(formula) == 2:
        if formula[0] == '-' and formula[1] in alpha:
            result = True
        else:
            result = False

    else:
        # Calls anotehr function that gets the symbol, left child, and the
        # right child of the formula.
        check = get_symbol_children(formula)
        left_child = check[1]
        right_child = check[2]

        # If the symbol is '-', then the result is just the validty of the left
        # child.
        if check[0] == '-':
            result = validity(check[1])

        # Otherwise it is the AND of the validty of the left and right child.
        else:
            result = validity(check[1]) and validity(check[2])

    # Returns the result.
    return result


def get_symbol_children(formula):
    '''(str) -> tupple of str
    Given a string boolean expression, the function will return a tupple with
    the main operator, the left child expression, and the right child
    expression.
    REQ: length of formula must be greater than 1.
    >>> get_symbol_children('-x')
    ('-', 'x', None)
    >>> get_symbol_children('(x+y)')
    ('+', 'x', 'y')
    >>> get_symbol_children('((x+y)*x)')
    ('*', '(x+y)', 'x')
    >>> get_symbol_children('((x+y)*(x*y))')
    ('*', '(x+y)', '(x*y)')
    >>> get_symbol_children('(x*(x*y))')
    ('*', 'x', '(x*y)')
    >>> get_symbol_children('(x*-(x*y))')
    ('*', 'x', '-(x*y)')
    >>> get_symbol_children('(-x*(x*y))')
    ('*', '-x', '(x*y)')
    >>> get_symbol_children('(-x*((x*y)*(x+y)))')
    ('*', '-x', '((x*y)*(x+y))')
    >>> get_symbol_children('(-x*-((x*y)*(x+y)))')
    ('*', '-x', '-((x*y)*(x+y))')
    '''
    result = ()
    # If the first character in the formula is '-', then that becomes the
    # symbol the left child is everything after that and the right child is
    # None since NotTree's only have one child.
    if formula[0] == '-':
        symbol = '-'
        left_child = formula[1:]
        right_child = None
        result = (symbol, left_child, right_child)

    else:
        # If the first and last characters in the formula are correspoding
        # brackets, the function removes them.
        if formula[0] == '(' and formula[-1] == ')':
            new_formula = formula[1:-1]
        else:
            new_formula = formula

        # If there are corresponding brakets still in the formula, the function
        # calls another function that returns the index of the main operator.
        if '(' in new_formula and ')' in new_formula:
            symbol_index = get_index(new_formula, '(')
            symbol = new_formula[symbol_index]

        # If there aren't any corresponding brackets, the index of the main
        # operator is the length of the formula divided by 2.
        else:
            symbol_index = len(new_formula)//2
            if new_formula[symbol_index] == '-':
                symbol_index = symbol_index - 1
            symbol = new_formula[symbol_index]

        # The left child is everything before the main operator and the right
        # child is everything after.
        left_child = new_formula[:symbol_index]
        right_child = new_formula[symbol_index+1:]

    # The result is a tupple consisting of the symbol, the left child, and the
    # rigth child.
    result = (symbol, left_child, right_child)

    # Returns the result.
    return result


def get_index(formula, bracket):
    '''(str, str) -> int
    Given a string boolen expression and a type of circulr bracket, the
    function will return the index of the main operator.
    REQ: bracket can only by either '(' or ')'.
    REQ: formula must contain atleast one '(' and ')'.
    >>> get_index('(x+y)*x', '(')
    5
    >>> get_index('(x+y)*(x*y)', '(')
    5
    >>> get_index('x*(x*y)', '(')
    1
    >>> get_index('x*-(x*y)', '(')
    1
    >>> get_index('-x*(x*y)', '(')
    2
    >>> get_index('-x*((x*y)*(x+y))', '(')
    2
    >>> get_index('-x*-((x*y)*(x+y))', '(')
    2
    '''
    index = 0
    if bracket == '(':
        for i in range(len(formula)):
            if i < 4:
                # If i is less than 4 and the current character is '(', then
                # the symbol is to the left of the '(' unless the character to
                # the left is a '-', then the symbol index is 2 characters to
                # the left of '('.
                if formula[i] == '(':
                    if formula[i-1] == '-':
                        index = i - 2
                    else:
                        index = i - 1

                    # If the character to the left isn't an operator, the
                    # function calls itself trying another method to find the
                    # index of the symbol.
                    if formula[index] not in operators:
                        index = get_index(formula, ')')

                # If i is less than 4 and the current character is '-' and the
                # next character is '(', then the symbol is to the left of the
                # '-'.
                elif formula[i] == '-' and formula[i+1] == '(':
                    index = i - 1

                    # If the character to the left isn't an operator, the
                    # function calls itself trying another method to find the
                    # index of the symbol.
                    if formula[index] not in operators:
                        index = get_index(formula, ')')

    # Other method of getting the index of the symbol.
    elif bracket == ')':
        # Finds the first occurance of '(' in the formula.
        first_index = formula.index('(')
        # Finds its corresponding bracket.
        corresponding_index = corresponding(formula)

        # Goes through all the keys in the dictionary until it find ones that
        # is the same as the index of the first '('.
        for key in corresponding_index:
            if key == first_index:
                # The symbol is to the right of the corresponding ')'.
                index = corresponding_index[key] + 1

    # Returns the result.
    return index


def corresponding(formula):
    '''(str) -> dict of int
    Given a formula, the function will return a dictionary with the keys being
    the index of all '(' and the value being the index of all ')'.
    REQ: formula must contain same number of '(' and ')'.
    >>> corresponding('(x+y)')
    {0: 4}
    >>> corresponding('((x+y)*x)')
    {0: 8, 1: 5}
    >>> corresponding('((x+y)*(x*y))')
    {0: 12, 1: 5, 7: 11}
    >>> corresponding('(x*(x*y))')
    {0: 8, 3: 7}
    >>> corresponding('(x*-(x*y))')
    {0: 9, 4: 8}
    >>> corresponding('(-x*(x*y))')
    {0: 9, 4: 8}
    >>> corresponding('(-x*((x*y)*(x+y)))')
    {0: 17, 11: 15, 4: 16, 5: 9}
    >>> corresponding('(-x*-((x*y)*(x+y)))')
    {0: 18, 12: 16, 5: 17, 6: 10}
    '''
    result = {}
    index = []

    for i in range(len(formula)):
        # The character equals the current character in the formula.
        character = formula[i]
        # If the character is ')', then the function removes the element from
        # the list and uses it as the key and the values is i.
        if character == ')':
            result[index.pop()] = i

        # If the character is '(', then the function stores the index of it.
        elif character == '(':
            index.append(i)

    # Returns the result.
    return result


def draw_formula_tree(root, count=0):
    '''(FormulaTree) -> str
    Given a FormulaTree, the function will return a string representation of
    the tree.
    >>> draw_formula_tree(build_tree('x'))
    'x'
    >>> draw_formula_tree(build_tree('-x'))
    '- x'
    >>> draw_formula_tree(build_tree('(x+y)'))
    '+ y\n  x'
    >>> draw_formula_tree(build_tree('((x+y)*x)'))
    '* x\n  + y\n    x'
    >>> draw_formula_tree(build_tree('((x+y)*(x*y))'))
    '* * y\n    x\n  + y\n    x'
    >>> draw_formula_tree(build_tree('(x*(x*y))'))
    '* * y\n    x\n  x'
    >>> draw_formula_tree(build_tree('(x*-(x*y))'))
    '* - * y\n      x\n  x'
    >>> draw_formula_tree(build_tree('(-x*(x*y))'))
    '* * y\n    x\n  - x'
    >>> draw_formula_tree(build_tree('(-x*((x*y)*(x+y)))'))
    '* * + y\n      x\n    * y\n      x\n  - x'
    >>> draw_formula_tree(build_tree('(-x*-((x*y)*(x+y)))'))
    '* - * + y\n        x\n      * y\n        x\n  - x'
    '''
    # If the root is None, the tree is just an empty string.
    if root is None:
        tree = ''

    # If the root isn't None, the function checks which instance the root is.
    else:
        # Depending on the instance, the tree equals the operator + the tree of
        # the right child + the tree of left child.

        # The count is increasd by 2 everytime the function goes in deeper into
        # the tree.

        # If the instance is a AndTree or an OrTree, anotehr function is called
        # that returns a string with a certain amount of spaces.
        if isinstance(root, AndTree):
            count += 2
            tree = ('*' + ' ' + draw_formula_tree(root.children[1], count) +
                    '\n' + spaces(count) + draw_formula_tree(root.children[0],
                                                             count))

        elif isinstance(root, OrTree):
            count += 2
            tree = ('+' + ' ' + draw_formula_tree(root.children[1], count) +
                    '\n' + spaces(count) + draw_formula_tree(root.children[0],
                                                             count))

        # If the instance is a NotTree, the tree equals the operator + the tree
        # of the left child.
        elif isinstance(root, NotTree):
            count += 2
            tree = '-' + ' ' + draw_formula_tree(root.children[0], count)

        # If the instance is a Leaf, the tree equals the symbol at that Leaf.
        elif isinstance(root, Leaf):
            tree = root.symbol

    # Returns the tree.
    return tree


def spaces(count):
    '''(int) -> str
    Given a int number, the function will return a string with the same number
    of spaces as the integer given.
    >>> spaces(1)
    ' '
    >>> spaces(2)
    '  '
    >>> spaces(3)
    '   '
    '''
    spaces = ''
    # Adds a space for the length of the integer given.
    for i in range(count):
        spaces += ' '
    # Returns the spaces.
    return spaces


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int
    Given a FormulaTree, a string of variables, and a string of values, the
    function will determine the outcome of the root and return it.
    REQ: variables length must be greater than 0.
    REQ: values length must be greater than 0.
    REQ: vairbales length must be equal to values length.
    >>> evaluate(build_tree('x'), 'x', '1')
    1
    >>> evaluate(build_tree('-x'), 'x', '1')
    0
    >>> evaluate(build_tree('(x+y)'), 'xy', '10')
    1
    >>> evaluate(build_tree('((x+y)*x)'), 'xy', '10')
    1
    >>> evaluate(build_tree('((x+y)*(x*y))'), 'xy', '10')
    0
    >>> evaluate(build_tree('(x*(x*y))'), 'xy', '11')
    1
    >>> evaluate(build_tree('(x*-(x*y))'), 'xy', '10')
    1
    >>> evaluate(build_tree('(-x*(x*y))'), 'xy', '10')
    0
    >>> evaluate(build_tree('(-x*((x*y)*(x+y)))'), 'xy', '11')
    0
    >>> evaluate(build_tree('(-x*-((x*y)*(x+y)))'), 'xy', '10')
    0
    '''
    # If the root is None then the result equals False.
    if not(root):
        result = False

    else:
        # Depending on the instance, the result equals the result of the left
        # child */+ the result of the right child.
        if isinstance(root, AndTree):
            result = (evaluate(root.children[0], variables, values) and
                      evaluate(root.children[1], variables, values))

        elif isinstance(root, OrTree):
            result = (evaluate(root.children[0], variables, values) or
                      evaluate(root.children[1], variables, values))

        # If the instance is a NotTree, the result equals the not value of the
        # result of the left child.
        elif isinstance(root, NotTree):
            result = not(evaluate(root.children[0], variables, values))

        # If the instance is a Leaf, the result equal either 1 or 0 depending
        # on the value of the symbol.
        elif isinstance(root, Leaf):
            # Gets the index of the symbol inside variables.
            index = variables.index(root.symbol)
            # If the int value of the symbol equals 1, the result equals True
            # otherwise it equals False.
            if int(values[index]) == 1:
                result = True
            else:
                result = False

    # Converts the boolean result to an integer.
    if result:
        result = 1
    else:
        result = 0

    # Returns the result.
    return result


def play2win(root, turns, variables, values):
    '''(FormulaTree, str, str, str) -> int
    Given a FormulaTree, a string of turns, a string of variables, and a string
    of the values for the variables, the function will determine the best next
    move for the current player.
    REQ: root can't be None
    REQ: turns must be greater than 0, and can only contain 'E' and/or 'A'.
    REQ: variables must be greater than 0.
    REQ: Values can only contain 0's or 1's or can be empty.
    REQ: length of variables must be greater then the length of the values.
    REQ: length of turns must be the same as the length of variables.
    >>> play2win(build_tree('x'), 'EA', 'x', '')
    1
    >>> play2win(build_tree('x'), 'AA', 'x', '')
    0
    >>> play2win(build_tree('x'), 'EE', 'x', '')
    1
    >>> play2win(build_tree('-x'), 'EA', 'x', '')
    0
    >>> play2win(build_tree('-x'), 'AE', 'x', '')
    1
    >>> play2win(build_tree('(x+y)'), 'AE', 'xy', '1')
    1
    >>> play2win(build_tree('(x+y)'), 'EA', 'xy', '1')
    0
    >>> play2win(build_tree('(x+y)'), 'EE', 'xy', '1')
    1
    >>> play2win(build_tree('(x+y)'), 'AA', 'xy', '1')
    0
    >>> play2win(build_tree('(x+y)'), 'EE', 'xy', '')
    1
    >>> play2win(build_tree('(x+y)'), 'AA', 'xy', '')
    0
    '''
    # Calls another function to get all binary permuations of values.
    perm = perms(values, len(variables))
    turn = turns[len(values)]

    try:
        # If the root is a Leaf, E equals 1, A equals 0.
        if isinstance(root, Leaf):
            if turn == 'E':
                result = 1
            else:
                result = 0

        # If the root is a NotTree and its child is a Leaf, E equals 0,
        # A equals 1.
        elif isinstance(root, NotTree) and isinstance(root.children[0], Leaf):
            if turn == 'E':
                result = 0
            else:
                result = 1
        else:
            # Calls another function to evaluate the FormulaTree.
            evaluation = evaluate(root, variables, perm[0])
            # Depending on whos turn it is, the function will call itself AND
            # the desired output from the player.
            if turn == 'E':
                result = 1 or play2win(root, turns, variables, perm[1:])
            else:
                result = 0 or play2win(root, turns, variables, perm[1:])

    except:
        if turn == 'E':
            result = 1
        else:
            result = 0

    # Returns the result.
    return result


def perms(values, length):
    '''(str, int) -> list of str
    Given a string of old values given by the user, and the amount of variables
    , the function will return all binary permuation of the values.
    >>> perms('', 1)
    ['0', '1']
    >>> perms('', 2)
    ['00', '01', '10', '11']
    >>> perms('1', 2)
    ['10', '11']
    >>> perms('0', 3)
    ['000', '001', '010', '011']
    '''
    result = []
    # Calls another function to get all permuations of the new values.
    perm = list(perms_helper(length))

    # If the old values contain 0's or 1's, the function removes all function
    # that dont begin with the numbers in the old values.
    if len(values) > 0:
        for i in range(len(perm)):
            if values == perm[i][:len(values)]:
                result.append(perm[i])
    # If the old values is empty, the function just leaves the permuations as
    # they are.
    else:
        result = perm

    # Returns the result.
    return result


def perms_helper(values_length):
    '''(int) -> generator object
    Given the amount of values, the function will return an object that
    contains all binary permuation up to the length of the variables.
    REQ: values_length must be greater than 0.
    '''
    # Loops for 2 to the power of the length of the values.
    for i in range(2 ** values_length):
        # Gets the binary representation of the current index and the removes
        # the first 2 characters in the representaion.
        perm = bin(i)[2:]
        # Adds a certain amount of 0's to the front of the permutation so that
        # the length of the permuation is the same as the length of the values.
        perm = '0' * (values_length - len(perm)) + perm
        # Yields a generator object of the current permuation and moves on to
        # the next permutation.
        yield perm
