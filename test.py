import unittest

from src.components import is_character

class TestComponents(unittest.TestCase):
    def test_is_character(self):
        self.assertEqual(is_character('a'), True)
        self.assertEqual(is_character('as'), False)

from src.puzzle import validate_sudoku_string

class TestPuzzle(unittest.TestCase):
    def test_validate_sudoku_string(self):
        valid_puzzle = '________1________2________3________4________5________6________7________8________9'
        self.assertEqual(validate_sudoku_string(valid_puzzle), True)

if __name__ == '__main__':
    unittest.main()