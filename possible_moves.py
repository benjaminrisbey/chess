from board import board, format_board
from convert_coords import convert_coords


def possible_moves(start_coords, type):
    row, col = start_coords
    y_neg_spaces = 7 - row
    y_spaces = 7 - y_neg_spaces
    x_neg_spaces = 7 - col
    x_spaces = 7 - x_neg_spaces

    board[row][col] = "\033[34m\033[0m"

    board[6][7] = "\033[31m\033[0m"

    def load_straight_axes():
        loop_board(steps=y_neg_spaces, row=row, col=col, row_dir="pos")
        loop_board(steps=y_spaces, row=row, col=col, row_dir="neg")
        loop_board(steps=x_neg_spaces, row=row, col=col, col_dir="pos")
        loop_board(steps=x_spaces, row=row, col=col, col_dir="neg")

    def load_diagonal_axes():
        loop_board(
            steps=y_neg_spaces,
            row=row,
            col=col,
            col_dir="pos",
            row_dir="pos",
            steps_compare=x_neg_spaces,
        )
        loop_board(
            steps=y_neg_spaces,
            row=row,
            col=col,
            col_dir="neg",
            row_dir="pos",
            steps_compare=x_spaces,
        )
        loop_board(
            steps=y_spaces,
            row=row,
            col=col,
            col_dir="neg",
            row_dir="neg",
            steps_compare=x_spaces,
        )
        loop_board(
            steps=y_spaces,
            row=row,
            col=col,
            col_dir="neg",
            row_dir="neg",
            steps_compare=x_spaces,
        )
        loop_board(
            steps=y_spaces,
            row=row,
            col=col,
            col_dir="pos",
            row_dir="neg",
            steps_compare=x_neg_spaces,
        )

    if type == "rook":
        load_straight_axes()

    if type == "bishop":
        load_diagonal_axes()

    if type == "queen":
        load_diagonal_axes()
        load_straight_axes()

    # if type == "knight":
    #     r = row
    #     c = col
    #     if board[r + 1][c + 2] == "x":
    #         board[r + 1][c + 2] = "\033[32mx\033[0m"
    #     if board[r + 1][c - 2] == "x":
    #         board[r + 1][c - 2] = "\033[32mx\033[0m"
    #     if board[r - 1][c - 2] == "x":
    #         board[r - 1][c - 2] = "\033[32mx\033[0m"
    #     if board[r - 1][c + 2] == "x":
    #         board[r - 1][c + 2] = "\033[32mx\033[0m"
    #     if board[r + 2][c + 1] == "x":
    #         board[r + 2][c + 1] = "\033[32mx\033[0m"
    #     if board[r + 2][c - 1] == "x":
    #         board[r + 2][c - 1] = "\033[32mx\033[0m"
    #     if board[r - 2][c - 1] == "x":
    #         board[r - 2][c - 1] = "\033[32mx\033[0m"
    #     if board[r - 2][c + 1] == "x":
    #         board[r - 2][c + 1] = "\033[32mx\033[0m"

    print(format_board(board, True))


def loop_board(steps, row, col, row_dir=None, col_dir=None, steps_compare=0):
    limit = min(steps, steps_compare) if steps_compare else steps

    for i in range(limit):
        r = row
        c = col

        if row_dir == "pos":
            r = row + i + 1
        elif row_dir == "neg":
            r = row - i - 1

        if col_dir == "pos":
            c = col + i + 1
        elif col_dir == "neg":
            c = col - i - 1

        if board[r][c] == "x":
            board[r][c] = "\033[32mx\033[0m"
        else:
            break


start_c = ("e", 4)
s_c = convert_coords(start_c)

possible_moves(s_c, "knight")
