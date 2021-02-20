from src.puzzle import validate_sudoku_file

with open('io/start_puzzle.sudoku', 'r') as f:
    start_puzzle = f.read()

print(start_puzzle)