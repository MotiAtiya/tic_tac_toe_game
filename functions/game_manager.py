from .validations import input_int_number, check_range, check_availability, input_yes_or_not

WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

def reset_game():
    board = [None] * 9
    current_player = 'X'
    return board, current_player

def input_cell_number(board):
    while True:
        try:
            cell_number = input_int_number()
            check_range(cell_number, len(board))
            check_availability(board, cell_number)
            return cell_number
        except ValueError as e:
            print("Error:", e)

def update_board(board, cell_number, player):
    board[cell_number-1] = player

def change_player(player):
    if player == 'X':
        return 'O'
    return 'X'


def has_win(board):
    for a, b, c in WINNING_LINES:
        if board[a] and board[b] and board[c] and \
         board[a] == board[b] == board[c]:
            return True
    return False

def has_draw(board):
    return None not in board

def exit_game():
    print("bye")
    exit(0)

def play_again():
    while True:
        try:
            choice = input()
            input_yes_or_not(choice)
            return choice == 'y' or choice == 'Y'
        except ValueError as e:
            print("Error:", e)
    