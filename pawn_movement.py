from white_pieces import white_pieces_map
from black_pieces import black_pieces_map
from board import board


def is_empty(square, board):
    row, col = square
    return board[row][col] == "x"


def pawn_movement(start_coords, current_turn):
    valid_movements = []

    row, col = start_coords

    if current_turn == "White":
        direction = -1
        start_row = 6
        enemy = "b"
    else:
        direction = 1
        start_row = 1
        enemy = "w"

    # one square forward
    one_forward = (row + direction, col)
    if is_empty(one_forward, board):
        valid_movements.append(one_forward)

        # two squares forward if on starting rank
        if row == start_row:
            two_forward = (row + 2 * direction, col)
            if is_empty(two_forward, board):
                valid_movements.append(two_forward)

    left_take = (row + direction, col - 1)
    if not is_empty(left_take, board):
        valid_movements.append(left_take)

    right_take = (row + direction, col + 1)
    if not is_empty(right_take, board):
        valid_movements.append(right_take)

    return valid_movements
    # capture happens naturally by overwrite
