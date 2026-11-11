from .utils import clear_screen

COLORS = {
    'FAIL': '\033[91m',
    'BOLD': '\033[1m',
    'OKBLUE': '\033[94m',
    'ENDC': '\033[0m'
}

def print_value(index, val):
    if val is None:
        return f"[{index+1}]"
    if val == 'X':
        return f"{COLORS['FAIL']}{COLORS['BOLD']} X {COLORS['ENDC']}"
    if val == 'O':
        return f"{COLORS['OKBLUE']}{COLORS['BOLD']} O {COLORS['ENDC']}"

def print_board(board):
    clear_screen()
    print(f"""
       |       |
  {print_value(0, board[0])}  |  {print_value(1, board[1])}  |  {print_value(2, board[2])}
       |       |
-------+-------+------
       |       |
  {print_value(3, board[3])}  |  {print_value(4, board[4])}  |  {print_value(5, board[5])}
       |       |
-------+-------+------
       |       |
  {print_value(6, board[6])}  |  {print_value(7, board[7])}  |  {print_value(8, board[8])}
       |       |
    """)

def print_prompt(player):
    print(f"Player {player}, choose a cell (1-9): ")

def print_winner(player):
    print(f"Player {player} wins!")

def print_draw():
    print("It's a draw!")

def print_play_again():
    print("Do you want to play again? [y/n]")
