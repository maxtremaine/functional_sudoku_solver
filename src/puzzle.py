import json
import re

# Components

with open('src/puzzle_rules.json', 'r') as f:
    puzzle_rules = json.load(f)

def validate_sudoku_string(sudoku_string):
    """If a string is 81 digits or underscores, return True."""
    pattern = re.compile('^(_|[1-9]){81}$')
    if pattern.match(sudoku_string) == None:
        return False
    return True

def validate_cell_index(cell_index: int):
    """If an input is less than 81, return True."""
    if cell_index > 80:
        return False
    return True

def validate_group(group_string):
    if len(group_string) != 9:
        return False
    numbers = [ x for x in group_string if x != '_' ]
    number_set = { x for x in numbers }
    return len(numbers) == len(number_set)

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
    return lambda sudoku_string:[
        sudoku_string[cell_index] for cell_index in cell_indexes
    ]

# Composites

def validate_puzzle(sudoku_string):
    valid_string = validate_sudoku_string(sudoku_string)
    if not valid_string:
        return ( 'Invalid sudoku string.', None )

    group_indexes = [ x for x in puzzle_rules['groups'] ]
    groups = [ get_cell_values(x)(sudoku_string) for x in group_indexes ]
    group_strings = [ ''.join(x) for x in groups ]
    group_validities = [ validate_group(x) for x in group_strings ]
    invalid_results = [ x for x in group_validities if x == False ]
    is_valid = len(invalid_results) == 0

    return ( None, is_valid )


    
