from current_turn import is_white_turn

board = [0] * 8

for i in range(len(board)):
    board[i] = ["x"] * 8


def format_board(board):
    x_coordinate_labels = "    a b c d e f g h   \n"
    lines = []
    lines.append("\n")

    lines.append(x_coordinate_labels)

    for i, row in enumerate(board):
        rank = 8 - i if is_white_turn() else i + 1

        line_parts = [f"{rank}   "]

        for col in row:
            line_parts.append(f"{col} ")

        line_parts.append(f"  {rank}")
        lines.append("".join(line_parts))

    lines.append("")
    lines.append(x_coordinate_labels)

    lines.append(
        f"{'\033[31mBlack\033[0m' if not is_white_turn(
        ) else '\033[34mWhite\033[0m'} to move!\n"
    )

    return "\n".join(lines)


def clear_board(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = "x"
