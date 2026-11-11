from functions.printer import print_board, print_prompt, print_winner, print_draw, print_play_again
from functions.game_manager import reset_game, input_cell_number, update_board, change_player, has_win, has_draw, exit_game, play_again

def main():
    while True:
        board, current_player = reset_game()

        while True:
            print_board(board)
            print_prompt(current_player)
            cell_number = input_cell_number(board)
            update_board(board, cell_number, current_player)

            if has_win(board):
                print_board(board)
                print_winner(current_player)
                print_play_again()
                if play_again():
                    break
                exit_game()
            if has_draw(board):
                print_board(board)
                print_draw()
                print_play_again()
                if play_again():
                    break
                exit_game()
                
            current_player = change_player(current_player)

if __name__ == "__main__":
    main()

