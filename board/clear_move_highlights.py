import re
from current_turn import is_white_turn
from board.board import board

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def remove_colour(text):
    return ANSI_RE.sub("", text)


def clear_move_highlights():
    if not is_white_turn():
        same_colour = "31"
    else:
        same_colour = "34"

    for x in range(8):
        for y in range(8):
            if board[x][y].startswith("\033[32m") or board[x][y].startswith("\033[33m"):
                piece = board[x][y]
                reset_piece = remove_colour(piece)
                if reset_piece != "x":
                    board[x][y] = f"\033[{same_colour}m{reset_piece}\033[0m"
                else:
                    board[x][y] = reset_piece
