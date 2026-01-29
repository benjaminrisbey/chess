from convert_coords import convert_coords
from pawn_movement import pawn_movement


valid_x_coordinates = ["a", "b", "c", "d", "e", "f", "g", "h"]
valid_y_coordinates = ["1", "2", "3", "4", "5", "6", "7", "8"]


def validate_input(user_input):
    if len(user_input) != 2:
        return False, "Input must be exactly 2 characters (e.g. 'e2')."

    x, y = user_input[0], user_input[1]

    if x not in valid_x_coordinates or y not in valid_y_coordinates:
        return False, f"'{user_input}' is not a valid board coordinate."

    return True, ""


def validate_movement(start_coords, end_coords, current_turn):
    start = convert_coords(start_coords)
    end = convert_coords(end_coords)

    if end in pawn_movement(start, current_turn):
        return True, ""

    return False, f"Invalid Movement {start_coords} -> {end_coords}"


def validate_piece(selected_square, current_turn, board):
    r, c = convert_coords(selected_square)
    piece = board[r][c]

    if piece == "x":
        return False, "No piece on that square"

    if current_turn and not piece.startswith("\033[34m"):
        return False, "Not White's piece"

    if not current_turn and not piece.startswith("\033[31m"):
        return False, "Not Black's piece"

    return True, ""


def validate_type(selected_square, board):
    r, c = convert_coords(selected_square)
    piece = board[r][c]

    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        return True, "Pawn"
    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        return True, "Bishop"
    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        return True, "Knight"
    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        return True, "Rook"
    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        return True, "Queen"
    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        return True, "King"
    return False, "Invalid piece"
