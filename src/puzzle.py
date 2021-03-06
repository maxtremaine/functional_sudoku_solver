import json
import re
from typing import Union, List, Tuple, Callable

# Load Sudoku puzzle rules.
with open('src/puzzle_rules.json', 'r') as f:
    puzzle_rules = json.load(f)

# Factories.
def Cell(index: int, value: str, sudoku_string: str) -> dict:
    related_values = get_related_numbers(sudoku_string)(index)
    return {
        'index': index,
        'value': value,
        'related_cells': get_related_cells(index),
        'related_values': related_values,
        'possible_values': missing_digits(related_values)
    }

# Working with Sudoku files and strings.

def validate_sudoku_file(sudoku_file:str) -> bool:
    pattern = re.compile('^(\s|\n|\||_|-|[1-9]|[a-i]){167}$')
    if pattern.match(sudoku_file) == None:
        return False
    return True

def validate_sudoku_string(sudoku_string: str) -> bool:
    """If a string is 81 digits or underscores, return True."""
    pattern = re.compile('^(_|[1-9]){81}$')
    if pattern.match(sudoku_string) == None:
        return False
    return True

def get_indexed_values(sudoku_string: str) -> Callable[[List[int]], List[str]]:
    return lambda indexes: [
        sudoku_string[index] for index in indexes
    ]

def missing_digits(values: List[str]) -> List[str]:
    """Returns the missing digits (from 1 to 9) as strings."""
    return [ str(x) for x in range(1, 10) if str(x) not in values ]

# Composites

def validate_puzzle(sudoku_string) -> Tuple[ str, bool ]:
    valid_string = validate_sudoku_string(sudoku_string)
    if not valid_string:
        return 'Invalid sudoku string.', False

    group_indexes = [ x for x in puzzle_rules['groups'] ]
    groups = [ get_indexed_values(sudoku_string)(x) for x in group_indexes ]
    group_strings = [ ''.join(x) for x in groups ]
    group_validities = [ validate_group(x) for x in group_strings ]
    invalid_results = [ x for x in group_validities if x == False ]
    is_valid = len(invalid_results) == 0

    return '', is_valid

def sudoku_file_to_string(sudoku_file: str) -> Tuple[str, str]:
    character_list = [
        sudoku_file[x]
        for x in puzzle_rules['file_to_string_conversion_indexes']
    ]
    sudoku_string = ''.join(character_list)
    is_valid_sudoku_string = validate_sudoku_string(sudoku_string)

    if not is_valid_sudoku_string:
        return 'Invalid sudoku string.', ''

    return '', sudoku_string

def sudoku_string_to_file(sudoku_string) -> Tuple[str, str]:
    empty_puzzle = puzzle_rules['empty_grid']
    

def cell_degrees_of_freedom(index: int) -> Callable[[str], Tuple[ str, int ]]:
    def _cell_degrees_of_freedom(sudoku_string):
        if not validate_sudoku_string(sudoku_string):
            return 'Invalid sudoku string.', 0

        related_cells = get_related_cells(index)
        cell_values = get_cell_values(sudoku_string)(related_cells)
        underscores = [ x for x in cell_values if x == '_' ]

        return '', len(underscores)
    
    return _cell_degrees_of_freedom

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

def get_related_numbers(sudoku_string: str) -> Callable[[int], List[str]]:
    return lambda cell_index: list({ 
        sudoku_string[x]
        for x in get_related_cells(cell_index)
        if sudoku_string[x] != '_'
    })