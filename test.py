import cube_functions

new_cube = cube_functions.create_cube()

rotations = [[4,1],[6,2],[1,1],[3,2],[5,1],[2,2]]

for idx in range(len(rotations)):
    new_cube = cube_functions.rotate_side(new_cube, rotations[idx][0], rotations[idx][1])

print(new_cube)

cube_explode = ''

for row in range(len(new_cube[0])):
    cube_explode = cube_explode + '   '
    for column in range(len(new_cube[0][row])):
        cube_explode += new_cube[0][row][column]
    cube_explode = cube_explode + '      \n'

middle = [4,3,5,2]

for row in range(len(new_cube[0])):
    for i in range(len(middle)):
        for column in range(len(new_cube[middle[i]][row])):
            cube_explode += new_cube[middle[i]][row][column]

    cube_explode += '\n'

for row in range(len(new_cube[1])):
    cube_explode = cube_explode + '   '
    for column in range(len(new_cube[1][row])):
        cube_explode += new_cube[1][row][column]
    cube_explode = cube_explode + '      \n'

print(cube_explode)
