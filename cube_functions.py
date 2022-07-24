import numpy as np
import enum

class Side(bytes, enum.Enum):
    def __new__(cls, value, face):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.face = face
        return obj
        
    up_face = (1, [[[],[2,0,2],[2,0,1],[2,0,0],[]],
            [[4,0,0],[0,0,0],[0,0,1],[0,0,2],[5,0,2]],
            [[4,0,1],[0,1,0],[0,1,1],[0,1,2],[5,0,1]],
            [[4,0,2],[0,2,0],[0,2,1],[0,2,2],[5,0,0]],
            [[],[3,0,0],[3,0,1],[3,0,2],[]]])

    down_face = (2, [[[],[3,2,0],[3,2,1],[3,2,2],[]],
            [[4,2,2],[1,0,0],[1,0,1],[1,0,2],[5,2,0]],
            [[4,2,1],[1,1,0],[1,1,1],[1,1,2],[5,2,1]],
            [[4,2,0],[1,2,0],[1,2,1],[1,2,2],[5,2,2]],
            [[],[2,2,2],[2,2,1],[2,2,0],[]]])

    back_face = (3, [[[],[0,0,2],[0,0,1],[0,0,0],[]],
            [[5,0,2],[2,0,0],[2,0,1],[2,0,2],[4,0,0]],
            [[5,1,2],[2,1,0],[2,1,1],[2,1,2],[4,1,0]],
            [[5,2,2],[2,2,0],[2,2,1],[2,2,2],[4,2,0]],
            [[],[1,2,2],[1,2,1],[1,2,0],[]]])

    front_face = (4, [[[],[0,2,0],[0,2,1],[0,2,2],[]],
            [[4,0,2],[3,0,0],[3,0,1],[3,0,2],[5,0,0]],
            [[4,1,2],[3,1,0],[3,1,1],[3,1,2],[5,1,0]],
            [[4,2,2],[3,2,0],[3,2,1],[3,2,2],[5,2,0]],
            [[],[1,0,0],[1,0,1],[1,0,2],[]]])

    left_face = (5, [[[],[0,0,0],[0,1,0],[0,2,0],[]],
            [[2,0,2],[4,0,0],[4,0,1],[4,0,2],[3,0,0]],
            [[2,1,2],[4,1,0],[4,1,1],[4,1,2],[3,1,0]],
            [[2,2,2],[4,2,0],[4,2,1],[4,2,2],[3,2,0]],
            [[],[1,2,0],[1,1,0],[1,0,0],[]]])

    right_face = (6, [[[],[0,2,2],[0,1,2],[0,0,2],[]],
            [[3,0,2],[5,0,0],[5,0,1],[5,0,2],[2,0,0]],
            [[3,1,2],[5,1,0],[5,1,1],[5,1,2],[2,1,0]],
            [[3,2,2],[5,2,0],[5,2,1],[5,2,2],[2,2,0]],
            [[],[1,0,2],[1,1,2],[1,2,2],[]]])


def create_cube():
    '''
    side_notation = [0, 1, 2, 3, 4, 5]
    '''
    cube = np.empty((6,3,3), dtype=str)
    side_notation = ['W', 'Y', 'B', 'G', 'O', 'R']
    for side in range(len(cube)):
        for row in range(len(cube[side])):
            for column in range(len(cube[side][row])):
                cube[side][row][column] = side_notation[side]
    return cube


def rotate_side(cube, side, rotation):
    '''
    Side(side).face[siderow][sidecolumn]
    '''
    rotating_side = np.empty((5,5), dtype=str)
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

        return
