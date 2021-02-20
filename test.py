import unittest

from src.components import is_character, change_character

class TestComponents(unittest.TestCase):
    def test_is_character(self):
        self.assertTrue(is_character('a'))
        self.assertFalse(is_character('as'))

    def test_change_character(self):
        self.assertEqual(change_character(0, 'a')('xxx'), 'axx')

from src.puzzle import (
    validate_sudoku_string,
    validate_sudoku_file
)

class TestPuzzle(unittest.TestCase):
    def test_validate_sudoku_string(self):
        valid_puzzle = '________1________2________3________4________5________6________7________8________9'
        self.assertTrue(validate_sudoku_string(valid_puzzle))
    
    def test_validate_sudoku_file(self):
        valid_file = '  abc def ghi\n1 7__|_4_|__1\n2 __1|___|2__\n3 _6_|2_9|_8_\n  -----------\n4 __3|5_4|9__\n5 1__|___|__4\n6 __2|1_8|5__\n  -----------\n7 _1_|9_6|_7_\n8 __8|___|4__\n9 6__|_2_|__8'
        invalid_file = '  wbc def ghi\n1 7__|_4_|__1\n2 __1|___|2__\n3 _6_|2_9|_8_\n  -----------\n4 __3|5_4|9__\n5 1__|___|__4\n6 __2|1_8|5__\n  -----------\n7 _1_|9_6|_7_\n8 __8|___|4__\n9 6__|_2_|__8 '
        self.assertTrue(validate_sudoku_file(valid_file))
        self.assertFalse(validate_sudoku_file(invalid_file))

if __name__ == '__main__':
    unittest.main()