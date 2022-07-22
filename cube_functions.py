import numpy as np

up_face = [[[],[2,0,2],[2,0,1],[2,0,0],[]],
            [[4,0,0],[0,0,0],[0,0,1],[0,0,2],[5,0,2]],
            [[4,0,1],[0,1,0],[0,1,1],[0,1,2],[5,0,1]],
            [[4,0,2],[0,2,0],[0,2,1],[0,2,2],[5,0,0]],
            [[],[3,0,0],[3,0,1],[3,0,2],[]]]

down_face = [[[],[2,2,0],[2,2,1],[2,2,2],[]],
            [[4,2,2],[1,0,0],[1,0,1],[1,0,2],[5,2,0]],
            [[4,2,1],[1,1,0],[1,1,1],[1,1,2],[5,2,1]],
            [[4,2,0],[1,2,0],[1,2,1],[1,2,2],[5,2,2]],
            [[],[3,2,1],[3,2,1],[3,2,0],[]]]

back_face = [[[],[0,0,2],[0,0,1],[0,0,0],[]],
            [[5,0,2],[2,0,0],[2,0,1],[2,0,2],[4,0,0]],
            [[5,1,2],[2,1,0],[2,1,1],[2,1,2],[4,1,0]],
            [[5,2,2],[2,2,0],[2,2,1],[2,2,2],[4,2,0]],
                [[],[1,2,2],[1,2,1],[1,2,0],[]]]

front_face = [[[],[0,2,0],[0,2,1],[0,2,2],[]],
            [[4,0,2],[3,0,0],[3,0,1],[3,0,2],[5,0,0]],
            [[4,1,2],[3,1,0],[3,1,1],[3,1,2],[5,1,0]],
            [[4,2,2],[3,2,0],[3,2,1],[3,2,2],[5,2,0]],
            [[],[1,0,0],[1,0,1],[1,0,2],[]]]

left_face = [[[],[0,0,0],[0,1,0],[0,2,0],[]],
            [[2,0,2],[4,0,0],[4,0,1],[4,0,2],[3,0,0]],
            [[2,1,2],[4,1,0],[4,1,1],[4,1,2],[3,1,0]],
            [[2,2,2],[4,2,0],[4,2,1],[4,2,2],[3,2,0]],
            [[],[1,2,0],[1,1,0],[1,0,0],[]]]

right_face = [[[],[0,2,2],[0,1,2],[0,0,2],[]],
            [[3,0,2],[5,0,0],[5,0,1],[5,0,2],[2,0,0]],
            [[3,1,2],[5,1,0],[5,1,1],[5,1,2],[2,1,0]],
            [[3,2,2],[5,2,0],[5,2,1],[5,2,2],[2,2,0]],
            [[],[1,0,2],[1,1,2],[1,2,2],[]]]


def create_cube():

    cube = np.empty(54, dtype=int).reshape(6,3,3)

    # side_notation = ['W', 'Y', 'B', 'G', 'O', 'R']
    side_notation = [0, 1, 2, 3, 4, 5]

    for side in range(len(cube)):
        for row in range(len(cube[side])):
            for column in range(len(cube[side][row])):
                cube[side][row][column] = side_notation[side]
    return cube


def rotate_side(cube, side, rotation):

    side_chosen = eval(side+"_face")

    current_cube_side = np.empty(25, dtype=int).reshape(5,5)

    for row in range(len(current_cube_side)):
        for column in range(len(current_cube_side[row])):
            index = side_chosen[row][column]
            if index:
                current_cube_side[row][column] = cube[index[0]][index[1]][index[2]]
            else:
                current_cube_side[row][column] = 7

    if rotation.startswith('c'):
        current_cube_side = np.rot90(current_cube_side, k=3)
    else:
        current_cube_side = np.rot90(current_cube_side, k=1)

    for row in range(len(current_cube_side)):
        for column in range(len(current_cube_side[row])):
            index = side_chosen[row][column]
            if index:
                cube[index[0]][index[1]][index[2]] = current_cube_side[row][column]
            else:
                continue
    return cube