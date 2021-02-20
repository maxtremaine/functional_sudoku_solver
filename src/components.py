from typing import Callable, List
from functools import reduce

# Composition

def pipe(*fs):
    return lambda x: reduce(lambda v, f: f(v), fs, x)

def map(fnc):
    return lambda xs: [ fnc(x) for x in xs ]

# Assertion

def is_character(string: str) -> bool:
    return len(string) == 1

def less_than_81(cell_index: int) -> bool:
    """If an input is less than 81, return True."""
    if cell_index < 81:
        return True
    return False

# Pure Functions

def change_character(index: int, value: str) -> Callable[[str], str]:
    """Changes a character in a string."""
    return lambda string: string[0:index] + value + string[index + 1:]

def indexes_of_substring(substring: str) -> Callable[[str], List[int]]:
    """Finds all indexes of a substring in a string."""
    return lambda string: [ i for (x, i) in zip(string, range(len(string))) if x == substring ]

def count_substring(substring: str) -> Callable[[str], int]:
    """Counts the instances of a substring in a string."""
    return lambda string: len(indexes_of_substring(substring)(string))