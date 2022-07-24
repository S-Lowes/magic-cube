import cube_functions

new_cube = cube_functions.create_cube()
rotations = [[4,1],[6,2],[1,1],[3,2],[5,1],[2,2]]

for idx in range(len(rotations)):
    new_cube = cube_functions.rotate_side(new_cube, rotations[idx][0], rotations[idx][1])
print(cube_functions.exploded_view(new_cube))

opposite_rotations = [[2,1],[5,2],[3,1],[1,2],[6,1],[4,2]]

for idx in range(len(opposite_rotations)):
    new_cube = cube_functions.rotate_side(new_cube, opposite_rotations[idx][0], opposite_rotations[idx][1])
print(cube_functions.exploded_view(new_cube))
