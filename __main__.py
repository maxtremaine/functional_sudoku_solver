from src.puzzle import (
    Cell,
    sudoku_file_to_string,
    validate_sudoku_string
)
from src.components import (
    change_character,
    count_substring
)

with open('io/start_puzzle.sudoku', 'r') as f:
    start_puzzle = f.read()

puzzle_error, puzzle_string = sudoku_file_to_string(start_puzzle)

if puzzle_error:
    raise Exception(puzzle_error)

blank_cells = count_substring('_')(puzzle_string)
run = 1

while blank_cells != 0:
    underscores = [
        Cell(i, x, puzzle_string)
        for i, x in enumerate(puzzle_string)
        if x == '_'
    ]

    single_values = [
        x for x in underscores if len(x['possible_values']) == 1
    ]

    for cell in single_values:
        puzzle_string = change_character(cell['index'], cell['possible_values'][0])(puzzle_string)
    
    blank_cells = count_substring('_')(puzzle_string)

    print(f'Solved {str(len(single_values))} cells on run {str(run)}.')

    run += 1

print(puzzle_string)
print(validate_sudoku_string(puzzle_string))
