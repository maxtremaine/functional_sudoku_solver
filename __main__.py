from src.puzzle import validate_sudoku_file

# print(missing_digits(['1', '2']))

# print(switch_character(5, '5')('________1________2________3________4________5________6________7________8________9'))

# print(validate_puzzle('________1________2________3________4________5________6________7________8________9'))

with open('io/start_puzzle.sudoku', 'r') as f:
    text = f.read()
    print(validate_sudoku_file(text))