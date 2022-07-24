# Magic Cube

This repository will simulate a Rubik's Cube (Magic Cube).

1. cube_functions.py - Module that will create, rotate & generate an exploded view of a Rubik's Cube.
1. cube_simulations.py - Simulate rotating a cube by choosing the side and rotation.
1. cube_test.py - Tests cube_functions.py module.

## Taking The Project Further (Additional Features)

- Represent Cube Differently to a 6x3x3 Matrix. (eg. Composite Representation 5x12)
- Create a different rotation method due to different cube representation.
- Add functionality for different cube size & shapes.

## Frameworks, Libraries, Programs & Technologies Used

- [Numpy](https://numpy.org/doc/stable/index.html)
- [ANSI](https://en.wikipedia.org/wiki/ANSI_escape_code)

## Testing

All Python code was written to be PEP8 compliant with the final code being tested with the command python3 -m flake8.

Aside from manually checking my code I created a small cube_test.py file.

- After making a series of delibrate rotations on a Cube it compares that with an expected result.
- The reverse rotations are made and checked against an untouched cube.

## Forking, Cloning

### Forking the GitHub Repository

By forking the GitHub Repository we are making a copy of the original repository on a GitHub account to view and/or make changes without affecting the original repository. This is done with the following steps:

- Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
- At the top of the Repository just above the "Settings" button on the menu, locate the "Fork" button.
- Click the button and now you should have a copy of the original repository in your GitHub account.

### Making a Local Clone

- Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
- Under the repository name, click "Code".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location that you want the cloned directory to be made.
- Type `git clone`, and then paste the URL you copied earlier.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation of the cloning process.