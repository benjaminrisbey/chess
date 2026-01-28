from convert_coords import convert_coords
from pawn_movement import black_pieces_map, pawn_movement, white_pieces_map
from white_pieces import white_pieces_map
from black_pieces import black_pieces_map

from board import board

valid_x_coordinates = ["a", "b", "c", "d", "e", "f", "g", "h"]
valid_y_coordinates = ["1", "2", "3", "4", "5", "6", "7", "8"]
valid_movements = []


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

    if current_turn % 2 == 0:
        current_turn = "White"
    else:
        current_turn = "Black"

    if end in pawn_movement(start, current_turn):
        return True, ""

    return False, f"Invalid Movement {start_coords} -> {end_coords}"


def validate_piece(selected_piece, current_turn):
    pieces_map = white_pieces_map if current_turn else black_pieces_map
    coords = convert_coords(selected_piece)

    for pieces_name, squares_list in pieces_map.items():
        for square in squares_list:
            if squares_list[square][-1] == coords:
                return True, ""
    return False, "Invalid piece"
