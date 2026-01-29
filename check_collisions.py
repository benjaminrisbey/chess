from board import board, format_board
from convert_coords import convert_coords


def check_collisions(start_coords, end_coords):
    s_row, s_col = end_coords
    e_row, e_col = start_coords

    print(start_coords)
    print(end_coords)

    board[s_row][s_col] = "\033[34m\033[0m"

    board[3][3] = "\033[31m\033[0m"

    if s_col == e_col:
        print("vertical movement")
        if s_row < e_row:
            print("negative")
            for i in range(e_row - s_row):
                if board[s_row + i][s_col] == "x":
                    board[s_row + i][s_col] = "\033[32mx\033[0m"
                else:
                    print("invalid move")
                    break
        else:
            print("positive")
            for i in range(s_row - e_row):
                if board[s_row - i][s_col] == "x":
                    board[s_row - i][s_col] = "\033[32mx\033[0m"
                else:
                    print("invalid move")
                    break

    if s_row == e_row:
        print("horizontal movement")
        if s_col < e_col:
            print("negative")
            for i in range(e_col - s_col):
                print(i)
                if board[s_row][e_col - i] == "x":
                    board[s_row][e_col - i] = "\033[32mx\033[0m"
                else:
                    print("invalid move")
                    break
        else:
            print("positive")
            for i in range(s_col - e_col):
                print(i)
                if board[s_row][e_col + i] == "x":
                    board[s_row][e_col + i] = "\033[32mx\033[0m"
                else:
                    print("invalid move")
                    break
    print(format_board(board, True))


start_c = ("a", 4)
end_c = ("f", 4)

s_c = convert_coords(start_c)
e_c = convert_coords(end_c)

check_collisions(s_c, e_c)
