from board.board import board
from remove_colour import remove_colour
from current_turn import is_white_turn


def get_rook_moves(coords):
    x, y = coords
    possible_moves = []

    if is_white_turn():
        same_colour = "\033[34m"
    else:
        same_colour = "\033[31m"

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        for i in range(1, 8):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < 8 and 0 <= ny < 8:
                print("i ran")
                if board[nx][ny] == "x":
                    possible_moves.append((nx, ny))
                    piece = board[nx][ny]
                    clean_piece = remove_colour(piece)
                    board[nx][ny] = f"\033[32m{clean_piece}\033[0m"
                elif not board[nx][ny].startswith(same_colour):
                    possible_moves.append((nx, ny))
                    piece = board[nx][ny]
                    print(piece)
                    clean_piece = remove_colour(piece)
                    board[nx][ny] = f"\033[32m{clean_piece}\033[0m"
                    break
                else:
                    break
    return possible_moves
