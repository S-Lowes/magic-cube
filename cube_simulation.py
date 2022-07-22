import cube_functions

print("Simulating A Rubik's Cube")

begin = input("Do you want to Simulate the Cube? Yes/No \n").lower()
if begin.startswith('y'):
    new_cube = cube_functions.create_cube()
else:
    quit()

print("Cube Created\nTime to Rotate")

rotate = 'y'

while rotate.startswith('y'):
    print("What side would you like to rotate?\n1) Up\n2) Down\n3) Front\n4) Back\n5) Left\n6) Right")
    while True:
        try:
            r_side = int(input('Enter Side Number: '))
            if r_side > 0 and r_side < 7:
                print("Nice!")
                break
            else:
                print("Options between 1-6")
        except:
            print("That's not a valid option!")

    print("Which direction Of Rotation?\n1) Clockwise\n2) Anti-Clockwise")
    while True:
        try:
            r_dir = int(input("Enter Direction Number: "))
            if r_dir > 0 and r_dir < 3:
                print("Sweet!")
                break
            else:
                print("1 For Clockwise or 2 For Anti-Clockwise")
        except:
            print("That's not a valid option!")
    
    new_cube = cube_functions.rotate_side(new_cube,r_side, r_dir)

    rotate = input("Do you want to make another rotation? Yes/No \n").lower()


print(new_cube)