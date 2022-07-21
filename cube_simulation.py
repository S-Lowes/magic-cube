import cube_functions

print("Simulating A Rubik's Cube")

begin = input("Do you want to Simulate the Cube? Yes/No \n").lower()
if begin.startswith('y'):
    new_cube = cube_functions.create_cube()
else:
    quit()

print("Cube Created\nTime to Rotate")

rotate = 'yes'

while rotate.startswith('y'):

    r_side = input("What side Would you like to Rotate? Up, Down, Front, Back, Left, Right \n").lower()
    r_dir = input("What side Would you like to Rotate? Clockwise/Anti \n").lower()
    
    new_cube = cube_functions.rotate_side(new_cube,r_side, r_dir)

    rotate = input("Do you want to make another rotation? Yes/No \n").lower()


print(new_cube)