def piece_move(start, end, board):
    sr, sc = start
    er, ec = end

    moving_piece = board[sr][sc]

    board[er][ec] = moving_piece
    board[sr][sc] = "x"
