import json
import re

with open('src/puzzle_rules.json', 'r') as f:
    puzzle_rules = json.load(f)

def validate_sudoku_string(sudoku_string):
    """If a string is 81 digits or underscores, return True."""
    pattern = re.compile('^(_|[1-9]){81}$')
    if pattern.match(sudoku_string) == None:
        return False
    return True

