col_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}


def convert_coords(input):
    x, y = input
    x = col_map[x]
    y = 8 - int(y)
    x, y = y, x

    return (x, y)
