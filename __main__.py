from src.puzzle import (
    Cell,
    sudoku_file_to_string,
    validate_sudoku_string,
    validate_puzzle
)
from src.components import (
    change_character,
    count_substring
)
from time import time

t0 = time()

with open('io/start_puzzle.sudoku', 'r') as f:
    start_puzzle = f.read()

puzzle_error, puzzle_string = sudoku_file_to_string(start_puzzle)

if puzzle_error:
    raise Exception(puzzle_error)

solved = False
threads = [ puzzle_string ]

while not solved:
    new_threads = []

    for thread in threads:
        underscores = [
            Cell(i, x, thread)
            for i, x in enumerate(thread)
            if x == '_'
        ]

        if len(underscores) == 0:
            solved = True
            new_threads = [ thread ]
            break

        sorted_underscores = sorted(
            underscores,
            key = lambda x: len(x['possible_values'])
        )

        for possible_value in sorted_underscores[0]['possible_values']:
            new_thread = change_character(sorted_underscores[0]['index'], possible_value)(thread)
            new_threads.append(new_thread)

    if len(new_threads) > 200:
        print(f'{len(new_threads)} threads.')

    threads = new_threads

print(threads[0])
print(validate_sudoku_string(threads[0]))
print(f'Took {int(time() - t0)} seconds.')
