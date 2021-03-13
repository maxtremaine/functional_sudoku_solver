from src.puzzle import (
    sudoku_file_to_string
)

with open('io/start_puzzle.sudoku', 'r') as f:
    start_puzzle = f.read()

puzzle_error, puzzle_string = sudoku_file_to_string(start_puzzle)

print(bool(puzzle_error), puzzle_string)
