import cube_functions

solved_cube = cube_functions.create_cube()
test_cube = cube_functions.create_cube()
rotations = [[4, 1], [6, 2], [1, 1], [3, 2], [5, 1], [2, 2]]

for idx in range(len(rotations)):
    test_cube = cube_functions.rotate_side(
        test_cube, rotations[idx][0], rotations[idx][1])

rotated_cube = cube_functions.exploded_view(test_cube)
expected_cube = open('magic-cube/expected_cube.txt', 'r')

if expected_cube.read() != rotated_cube:
    raise Exception("Rotation operation flawed")

print(rotated_cube)

opposite_rotations = [[2, 1], [5, 2], [3, 1], [1, 2], [6, 1], [4, 2]]

for idx in range(len(opposite_rotations)):
    test_cube = cube_functions.rotate_side(
        test_cube, opposite_rotations[idx][0], opposite_rotations[idx][1])

test_condition = True
while test_condition:
    if len(solved_cube) == len(test_cube):
        for side in range(len(test_cube)):
            for row in range(len(test_cube[side])):
                for column in range(len(test_cube[side][row])):
                    if solved_cube[side][row][column] != \
                         test_cube[side][row][column]:
                        raise Exception("Cubes Elements not identical")
        test_condition = False
    else:
        raise Exception("Cubes sizes miss matched")
print(cube_functions.exploded_view(test_cube))
