from board import board
from is_empty import is_empty


def pawn_movement(start_coords, is_white_turn):
    valid_movements = []

    row, col = start_coords

    if is_white_turn:
        direction = -1
        start_row = 6
    else:
        direction = 1
        start_row = 1

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
