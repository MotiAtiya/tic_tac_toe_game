def input_int_number():
    try:
        return int(input())
    except ValueError:
        raise ValueError("Insert only an interger number")

def check_range(number, valid_range):
    if not number in range(1, valid_range + 1):
        raise ValueError(f"Wrong number. Insert only between 1 - {valid_range}")

def check_availability(board, cell_number):
    if (board[cell_number-1]) is not None:
        raise ValueError(f"Cell {cell_number} already occupied. Please enter an available cell")

def input_yes_or_not(choice):
    if choice.lower() not in ['y','n']:
        raise ValueError("Insert only 'y' or 'n' please")
