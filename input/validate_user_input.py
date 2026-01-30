from convert_coords import convert_coords
from moves.get_bishop_moves import get_bishop_moves
from moves.get_knight_moves import get_knight_moves
from moves.get_rook_moves import get_rook_moves
from moves.get_queen_moves import get_queen_moves
from moves.get_king_moves import get_king_moves
from moves.get_pawn_moves import get_pawn_moves
from board.board import board
from remove_colour import remove_colour
from board.clear_move_highlights import clear_move_highlights


valid_x_coordinates = ["a", "b", "c", "d", "e", "f", "g", "h"]
valid_y_coordinates = ["1", "2", "3", "4", "5", "6", "7", "8"]

piece_possible_moves = []


def validate_select_input(selected_square, is_white_turn):
    if len(selected_square) != 2:
        return False, "Input must be exactly 2 characters (e.g. 'e2')."

    x, y = selected_square[0], selected_square[1]

    if x not in valid_x_coordinates or y not in valid_y_coordinates:
        return False, f"'{selected_square}' is not a valid board coordinate."

    r, c = convert_coords(selected_square)
    piece = board[r][c]

    if piece == "x":
        return False, "No piece on that square"

    if is_white_turn and not piece.startswith("\033[34m"):
        return False, "Incorrect colour"

    if not is_white_turn and not piece.startswith("\033[31m"):
        return False, "Incorecct colour"

    validate_type((r, c), is_white_turn)

    return True, ""


def validate_type(selected_square, is_white_turn):
    piece_possible_moves.clear()
    r, c = selected_square
    piece = board[r][c]
    highlighted_piece = remove_colour(piece)
    board[r][c] = f"\033[33m{highlighted_piece}\033[0m"

    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        for coord in get_pawn_moves((r, c), is_white_turn):
            piece_possible_moves.append(coord)
    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        for coord in get_bishop_moves((r, c), is_white_turn):
            piece_possible_moves.append(coord)

    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        for coord in get_knight_moves((r, c), is_white_turn):
            piece_possible_moves.append(coord)

    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        for coord in get_rook_moves((r, c), is_white_turn):
            piece_possible_moves.append(coord)

    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        for coord in get_queen_moves((r, c), is_white_turn):
            piece_possible_moves.append(coord)

    if piece == "\033[34m\033[0m" or piece == "\033[31m\033[0m":
        for coord in get_king_moves((r, c), is_white_turn):
            piece_possible_moves.append(coord)

    # print(piece_possible_moves)

    return False, "Invalid piece"


def validate_move_input(selected_square, is_white_turn):
    if len(selected_square) != 2:
        return False, "Input must be exactly 2 characters (e.g. 'e2')."

    x, y = selected_square[0], selected_square[1]

    if x not in valid_x_coordinates or y not in valid_y_coordinates:
        return False, f"'{selected_square}' is not a valid board coordinate."

    clear_move_highlights(is_white_turn)

    return True, ""
