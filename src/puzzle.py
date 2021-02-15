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

def validate_cell_index(cell_index):
    """If an input is less than 81, return True."""
    try:
        if cell_index > 80:
            return False
    except:
        return False
    return True

def get_related_cells(cell_index):
    """Returns a list of related cells."""
    related_groups = [
        n for n in puzzle_rules['groups']
        if cell_index in n
    ]
    related_cells = [
        y for x in related_groups for y in x
    ]
    unique_related_cells = {
        x for x in related_cells
    }
    return list(unique_related_cells)

def get_cell_values(cell_indexes):
    def _(sudoku_string):
        return [
            sudoku_string[cell_index] for cell_index in cell_indexes
        ]
    return _

print(get_cell_values([1, 2, 3])('0174'))