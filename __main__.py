from src.puzzle import validate_puzzle, sudoku_file_to_string

# print(missing_digits(['1', '2']))

# print(switch_character(5, '5')('________1________2________3________4________5________6________7________8________9'))

print(validate_puzzle('________1________2________3________4________5________6________7________8________9'))

with open('io/start_puzzle.sudoku', 'r') as f:
    string = sudoku_file_to_string(f.read())