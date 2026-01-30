from pieces.white_pieces import white_pieces_map
from pieces.black_pieces import black_pieces_map


def load_pieces(board):
    # White
    for symbol, pieces in white_pieces_map.items():
        for squares in pieces.values():
            x, y = squares[-1]
            board[x][y] = symbol

    # Black
    for symbol, pieces in black_pieces_map.items():
        for squares in pieces.values():
            x, y = squares[-1]
            board[x][y] = symbol
