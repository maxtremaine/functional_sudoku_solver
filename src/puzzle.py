import re

def validate_sudoku_string(sudoku_string):
    pattern = re.compile('(_|[1-9]){81}')
    return pattern.match(sudoku_string)