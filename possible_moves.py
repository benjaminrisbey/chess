from board import board, format_board
from convert_coords import convert_coords


def check_collisions(start_coords):
    row, col = start_coords
    y_neg_spaces = 7 - row
    y_spaces = 7 - y_neg_spaces
    x_neg_spaces = 7 - col
    x_spaces = 7 - x_neg_spaces

    print(start_coords)

    board[row][col] = "\033[34m\033[0m"

    board[5][5] = "\033[31m\033[0m"

    print("vertical movement")
    for i in range(y_neg_spaces):
        if board[row + i + 1][col] == "x":
            board[row + i + 1][col] = "\033[32mx\033[0m"
        else:
            break

    for i in range(y_spaces):
        if board[row - i - 1][col] == "x":
            board[row - i - 1][col] = "\033[32mx\033[0m"
        else:
            break

    print("horizontal movement")
    for i in range(x_neg_spaces):
        if board[row][col + i + 1] == "x":
            board[row][col + i + 1] = "\033[32mx\033[0m"
        else:
            break
    for i in range(x_spaces):
        if board[row][col - i - 1] == "x":
            board[row][col - i - 1] = "\033[32mx\033[0m"
        else:
            break

    print("diagonal movement")
    print("negative")

    for i in range(y_neg_spaces if y_neg_spaces < x_neg_spaces else x_neg_spaces):
        if board[row + i + 1][col + i + 1] == "x":
            board[row + i + 1][col + i + 1] = "\033[32mx\033[0m"
        else:
            break

    for i in range(y_neg_spaces if y_neg_spaces < x_spaces else x_spaces):
        if board[row + i + 1][col - i - 1] == "x":
            board[row + i + 1][col - i - 1] = "\033[32mx\033[0m"
        else:
            break

    print("positive")
    for i in range(y_spaces if y_spaces < x_spaces else x_spaces):
        if board[row - i - 1][col - i - 1] == "x":
            board[row - i - 1][col - i - 1] = "\033[32mx\033[0m"
        else:
            break

    for i in range(y_spaces if y_spaces < x_neg_spaces else x_neg_spaces):
        if board[row - i - 1][col + i + 1] == "x":
            board[row - i - 1][col + i + 1] = "\033[32mx\033[0m"
        else:
            break

    print(format_board(board, True))


start_c = ("e", 4)
s_c = convert_coords(start_c)

check_collisions(s_c)
