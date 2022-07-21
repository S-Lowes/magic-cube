import numpy as np
import cube_side_select
import enum

# class sides(enum.Enum):
#    up = 0
#    down = 1
#    back = 2
#    front = 3
#    left = 4
#    right = 5
# # print(sides.up.value)

cube = np.empty(54, dtype=int).reshape(6,3,3)

# side_notation = ['W', 'Y', 'B', 'G', 'O', 'R']
side_notation = [0, 1, 2, 3, 4, 5]

# The color of a face is indexed like cube[SIDE][ROW][COL]
for side in range(len(cube)):
    for row in range(len(cube[side])):
        for column in range(len(cube[side][row])):
            cube[side][row][column] = side_notation[side]


side = str(input("What Side to Rotate?\n "))
rotation = str(input("Which Direction?\n "))

side_co = cube_side_select.side_select(side)

current_cube_side = np.empty(25, dtype=int).reshape(5,5)

for row in range(len(current_cube_side)):
    for column in range(len(current_cube_side[row])):
        if len(side_co[row][column]) != 0:
            current_cube_side[row][column] = eval("cube"+side_co[row][column])
        else:
            current_cube_side[row][column] = 7

print(current_cube_side)

if rotation == "clockwise":
    current_cube_side = np.rot90(current_cube_side, k=3)
if rotation == "anti-clockwise":
    current_cube_side = np.rot90(current_cube_side, k=1)

print(current_cube_side)

for row in range(len(current_cube_side)):
    for column in range(len(current_cube_side[row])):
        if len(side_co[row][column]) != 0:
            exec("cube"+side_co[row][column] + "=" + str(current_cube_side[row][column]))
        else:
            continue

print (cube)