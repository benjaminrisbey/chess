from board.board import board, format_board
from board.load_game import load_pieces
from input.validate_user_input import validate_select_input, validate_move_input
from moves.piece_move import piece_move
from convert_coords import convert_coords
from board.clear_move_highlights import clear_move_highlights
from current_turn import is_white_turn, update_current_turn
import os

current_turn = 0
status_message = ""
input_message = ""
load_pieces(board)


invalid_user_piece_input = True
invalid_user_move_input = True


def render():
    # os.system("clear")
    print(format_board(board if is_white_turn() else board[::-1]))

    if status_message:
        print("\033[A", end="")
        print(status_message)


while True:
    invalid_user_piece_input = True
    invalid_user_move_input = True
    status_message = ""
    select_piece = ""
    move_square = ""

    print(is_white_turn())

    select_x = 9
    select_y = 9
    move_x = 9
    move_y = 9

    # Select piece
    while invalid_user_piece_input:
        render()

        select_piece = input("Piece to Move: ").lower()
        is_valid_select_input, message = validate_select_input(select_piece)

        if is_valid_select_input:
            invalid_user_piece_input = False

        status_message = message

    # Select move
    while invalid_user_move_input:
        render()

        move_square = input("Where to Move: ").lower()

        if move_square == "":
            clear_move_highlights()
            break
        is_valid_move_input, message = validate_move_input(move_square)

        if is_valid_move_input:
            invalid_user_move_input = False

        status_message = message

    if move_square:
        piece_move(convert_coords(select_piece), convert_coords(move_square))
        current_turn += 1
        update_current_turn(current_turn)
