from src.puzzle import (
    sudoku_file_to_string,
    cell_degrees_of_freedom
)

with open('io/start_puzzle.sudoku', 'r') as f:
    start_puzzle = f.read()

puzzle_string = sudoku_file_to_string(start_puzzle)
degs = cell_degrees_of_freedom(4)(puzzle_string)

print(degs)