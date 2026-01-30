from board import board, format_board
from load_game import load_pieces
from validate_user_input import validate_select_input, validate_move_input
from piece_move import piece_move
from convert_coords import convert_coords
import os

current_turn = 0
status_message = ""
input_message = ""
load_pieces(board)


invalid_user_piece_input = True
invalid_user_move_input = True


def is_white_turn(current_turn):
    return current_turn % 2 == 0


def render():
    os.system("clear")
    print(
        format_board(
            board if is_white_turn(current_turn) else board[::-1],
            is_white_turn(current_turn),
        )
    )

    if status_message:
        print("\033[A", end="")
        print(status_message)


while True:
    invalid_user_piece_input = True
    invalid_user_move_input = True
    status_message = ""
    select_piece = ""
    move_square = ""

    select_x = 9
    select_y = 9
    move_x = 9
    move_y = 9

    # Select piece
    while invalid_user_piece_input:
        render()

        select_piece = input("Piece to Move: ").lower()
        is_valid_select_input, message = validate_select_input(
            select_piece, is_white_turn(current_turn)
        )

        if is_valid_select_input:
            invalid_user_piece_input = False

        status_message = message

    # Select move
    while invalid_user_move_input:
        render()

        move_square = input("Where to Move: ").lower()
        is_valid_move_input, message = validate_move_input(
            move_square, is_white_turn(current_turn)
        )

        if is_valid_move_input:
            invalid_user_move_input = False

        status_message = message

    piece_move(convert_coords(select_piece),
               convert_coords(move_square), board)
    current_turn += 1
