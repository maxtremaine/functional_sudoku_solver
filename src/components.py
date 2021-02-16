from typing import Callable, List

def is_character(string: str) -> bool:
    return len(string) == 1

def less_than_81(cell_index: int) -> bool:
    """If an input is less than 81, return True."""
    if cell_index < 81:
        return True
    return False

def change_character(index: int, value: str) -> Callable[[str], str]:
    """Changes a character in a string."""
    return lambda string: (
        string[0:index] + value + string[index + 1:]
    )

def indexes_of_character(character: str) -> Callable[[str], List[int]]:
    """Finds all indexes of a character in a string."""
    return lambda string: [ i for (x, i) in zip(string, range(len(string))) if x == character ]