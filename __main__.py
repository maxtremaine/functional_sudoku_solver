from src.puzzle import (
    sudoku_file_to_string,
    cell_degrees_of_freedom
)

with open('io/start_puzzle.sudoku', 'r') as f:
    start_puzzle = f.read()

puzzle_string = sudoku_file_to_string(start_puzzle)

underscores = [
    {
        'index': i,
        'value': x,
        'degrees_of_freedom': cell_degrees_of_freedom(i)(puzzle_string)
    }
    for i, x in enumerate(puzzle_string)
    if x == '_'
]

prioritized_underscores = sorted(
    underscores,
    key = lambda underscore: underscore['degrees_of_freedom'],
    reverse = True
)

print(prioritized_underscores)
