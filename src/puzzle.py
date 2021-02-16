import json
import re
from typing import Union, List, Tuple, Callable

# Components

with open('src/puzzle_rules.json', 'r') as f:
    puzzle_rules = json.load(f)

def validate_sudoku_string(sudoku_string: str) -> bool:
    """If a string is 81 digits or underscores, return True."""
    pattern = re.compile('^(_|[1-9]){81}$')
    if pattern.match(sudoku_string) == None:
        return False
    return True

def get_cell_values(cell_indexes: List[int]) -> Callable[[str], List[str]]:
    return lambda sudoku_string:[
        sudoku_string[cell_index] for cell_index in cell_indexes
    ]

def missing_digits(group_string: Union[List[str], str]) -> List[str]:
    """Returns the missing digits (from 1 to 9) as strings."""
    return [ str(x) for x in range(1, 10) if str(x) not in group_string ]

def sudoku_file_to_string(sudoku_file: str) -> str:
    character_list = [
        sudoku_file[x]
        for x in puzzle_rules['file_to_string_conversion_indexes']
    ]
    return ''.join(character_list)

# Composites

def validate_puzzle(sudoku_string) -> Tuple[ Union[ str, None ], Union[ bool, None ] ]:
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

def cell_degrees_of_freedom(index):
    def wrapped(sudoku_string):
        if not validate_sudoku_string(sudoku_string):
            return ( 'Invalid sudoku string.', None )
    
def validate_group(group_string: str) -> bool:
    if len(group_string) != 9:
        return False
    numbers = [ x for x in group_string if x != '_' ]
    number_set = { x for x in numbers }
    return len(numbers) == len(number_set)

def get_related_cells(cell_index: int) -> List[int]:
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