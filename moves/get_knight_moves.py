from board.board import board
from remove_colour import remove_colour


def get_knight_moves(coords, is_white_turn):
    row, col = coords
    possible_moves = []

    if is_white_turn:
        same_colour = "\033[34m"
    else:
        same_colour = "\033[31m"

    offsets = [
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
    ]

    for dx, dy in offsets:
        nx, ny = row + dx, col + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            if not board[nx][ny].startswith(same_colour):
                possible_moves.append((nx, ny))
                piece = board[nx][ny]
                clean_piece = remove_colour(piece)
                board[nx][ny] = f"\033[32m{clean_piece}\033[0m"

    return possible_moves
