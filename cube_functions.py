# -----------------------------------------------------------
# Functions & Classes that create, rotate and generate an
# exploded view for a Magic Cube.
# -----------------------------------------------------------

import numpy as np
import enum


class Side(bytes, enum.Enum):
    """Create Side Class.

    Cube mapped as 6x3x3 Array. Enumerate the values
    affected by a rotation of a specific side.
    """
    def __new__(cls, value, face):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.face = face
        return obj

    up_face = (1, [[[], [2, 0, 2], [2, 0, 1], [2, 0, 0], []],
               [[4, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 2], [5, 0, 2]],
               [[4, 0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 2], [5, 0, 1]],
               [[4, 0, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [5, 0, 0]],
               [[], [3, 0, 0], [3, 0, 1], [3, 0, 2], []]])

    down_face = (2, [[[], [3, 2, 0], [3, 2, 1], [3, 2, 2], []],
                 [[4, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [5, 2, 0]],
                 [[4, 2, 1], [1, 1, 0], [1, 1, 1], [1, 1, 2], [5, 2, 1]],
                 [[4, 2, 0], [1, 2, 0], [1, 2, 1], [1, 2, 2], [5, 2, 2]],
                 [[], [2, 2, 2], [2, 2, 1], [2, 2, 0], []]])

    back_face = (3, [[[], [0, 0, 2], [0, 0, 1], [0, 0, 0], []],
                 [[5, 0, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [4, 0, 0]],
                 [[5, 1, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [4, 1, 0]],
                 [[5, 2, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2], [4, 2, 0]],
                 [[], [1, 2, 2], [1, 2, 1], [1, 2, 0], []]])

    front_face = (4, [[[], [0, 2, 0], [0, 2, 1], [0, 2, 2], []],
                  [[4, 0, 2], [3, 0, 0], [3, 0, 1], [3, 0, 2], [5, 0, 0]],
                  [[4, 1, 2], [3, 1, 0], [3, 1, 1], [3, 1, 2], [5, 1, 0]],
                  [[4, 2, 2], [3, 2, 0], [3, 2, 1], [3, 2, 2], [5, 2, 0]],
                  [[], [1, 0, 0], [1, 0, 1], [1, 0, 2], []]])

    left_face = (5, [[[], [0, 0, 0], [0, 1, 0], [0, 2, 0], []],
                 [[2, 0, 2], [4, 0, 0], [4, 0, 1], [4, 0, 2], [3, 0, 0]],
                 [[2, 1, 2], [4, 1, 0], [4, 1, 1], [4, 1, 2], [3, 1, 0]],
                 [[2, 2, 2], [4, 2, 0], [4, 2, 1], [4, 2, 2], [3, 2, 0]],
                 [[], [1, 2, 0], [1, 1, 0], [1, 0, 0], []]])

    right_face = (6, [[[], [0, 2, 2], [0, 1, 2], [0, 0, 2], []],
                  [[3, 0, 2], [5, 0, 0], [5, 0, 1], [5, 0, 2], [2, 0, 0]],
                  [[3, 1, 2], [5, 1, 0], [5, 1, 1], [5, 1, 2], [2, 1, 0]],
                  [[3, 2, 2], [5, 2, 0], [5, 2, 1], [5, 2, 2], [2, 2, 0]],
                  [[], [1, 0, 2], [1, 1, 2], [1, 2, 2], []]])


class Colour(bytes, enum.Enum):
    """Create Colour Class.

    Enumerate ANSI background colour for each side.
    """
    def __new__(cls, value, col_hex):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.col_hex = col_hex
        return obj

    White = (0, '\033[48;2;240;240;255mW ')
    Yellow = (1, '\033[48;2;250;250;50mY ')
    Blue = (2, '\033[48;2;55;130;230mB ')
    Green = (3, '\033[48;2;130;220;0mG ')
    Orange = (4, '\033[48;2;255;165;0mO ')
    Red = (5, '\033[48;2;220;60;50mR ')


def create_cube():
    """Create The Magic Cube.

    The Cube is initially an empty 6x3x3 numpy array before being replaced
    by the initial values for each side of a solved cube.
    """
    cube = np.empty((6, 3, 3), dtype=object)
    side_notation = ['White', 'Yellow', 'Blue', 'Green', 'Orange', 'Red']
    for side in range(len(cube)):
        for row in range(len(cube[side])):
            for column in range(len(cube[side][row])):
                cube[side][row][column] = side_notation[side]
    return cube


def rotate_side(cube, side, rotation):
    """Rotate the selected side given a selected rotation.

    Using the Side Class and numpy rot90 we can rotate a side of the cube.
    """
    rotating_side = np.empty((5, 5), dtype=object)
    for row in range(len(rotating_side)):
        for column in range(len(rotating_side[row])):
            index = Side(side).face[row][column]
            if index:
                rotating_side[row][column] = cube[index[0]][index[1]][index[2]]
            else:
                rotating_side[row][column] = ''

    if rotation == 1:
        rotating_side = np.rot90(rotating_side, k=3)
    else:
        rotating_side = np.rot90(rotating_side, k=1)

    for row in range(len(rotating_side)):
        for column in range(len(rotating_side[row])):
            index = Side(side).face[row][column]
            if index:
                cube[index[0]][index[1]][index[2]] = rotating_side[row][column]
            else:
                continue
    return cube


def exploded_view(cube):
    """Create an exploded view of the Magic Cube.

    Create a string with ANSI background colour using our Colour Class.
    """
    cube_explode = ''
    for row in range(len(cube[0])):
        cube_explode = cube_explode + '\033[49m      '
        for column in range(len(cube[0][row])):
            cube_explode += Colour[cube[0][row][column]].col_hex
        cube_explode = cube_explode + '\033[49m            \n'

    middle = [4, 3, 5, 2]
    for row in range(len(cube[0])):
        for i in range(len(middle)):
            for column in range(len(cube[middle[i]][row])):
                cube_explode += Colour[cube[middle[i]][row][column]].col_hex

        cube_explode += '\033[49m\n'

    for row in range(len(cube[1])):
        cube_explode = cube_explode + '\033[49m      '
        for column in range(len(cube[1][row])):
            cube_explode += Colour[cube[1][row][column]].col_hex
        cube_explode = cube_explode + '\033[49m            \n'

    return (cube_explode)
