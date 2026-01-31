check_white_turn = True


def update_current_turn(current_turn):
    global check_white_turn
    check_white_turn = current_turn % 2 == 0


def is_white_turn():
    return check_white_turn
