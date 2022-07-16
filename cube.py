import numpy as np

# name = input('Please Enter Your Name \n')
# print('Hi', name)

cube = np.empty(54, dtype=str).reshape(6,3,3)
side_notation = ['L', 'F', 'R', 'B', 'U', 'D']

# The color of a face is indexed like cube[SIDE][ROW][COL]
for side in range(len(cube)):
    for row in range(len(cube[side])):
        for column in range(len(cube[side][row])):
            cube[side][column][row] = side_notation[side]

print(cube)

# print("Make A Change")
# print(np.rot90(arr1, k=2, axes=(0,1)))