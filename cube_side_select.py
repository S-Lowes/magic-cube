import numpy as np

up_face = [["","[2][0][2]","[2][0][1]","[2][0][0]",""],
            ["[4][0][0]","[0][0][0]","[0][0][1]","[0][0][2]","[5][0][2]"],
            ["[4][0][1]","[0][1][0]","[0][1][1]","[0][1][2]","[5][0][1]"],
            ["[4][0][2]","[0][2][0]","[0][2][1]","[0][2][2]","[5][0][0]"],
            ["","[3][0][0]","[3][0][1]","[3][0][2]",""]]

down_face = [["","[2][2][0]","[2][2][1]","[2][2][2]",""],
            ["[4][2][2]","[1][0][0]","[1][0][1]","[1][0][2]","[5][2][0]"],
            ["[4][2][1]","[1][1][0]","[1][1][1]","[1][1][2]","[5][2][1]"],
            ["[4][2][0]","[1][2][0]","[1][2][1]","[1][2][2]","[5][2][2]"],
            ["","[3][2][1]","[3][2][1]","[3][2][0]",""]]

back_face = [["","[0][0][2]","[0][0][1]","[0][0][0]",""],
            ["[5][0][2]","[2][0][0]","[2][0][1]","[2][0][2]","[4][0][0]"],
            ["[5][1][2]","[2][1][0]","[2][1][1]","[2][1][2]","[4][1][0]"],
            ["[5][2][2]","[2][2][0]","[2][2][1]","[2][2][2]","[4][2][0]"],
                ["","[1][2][2]","[1][2][1]","[1][2][0]",""]]

front_face = [["","[0][2][0]","[0][2][1]","[0][2][2]",""],
            ["[4][0][2]","[3][0][0]","[3][0][1]","[3][0][2]","[5][0][0]"],
            ["[4][1][2]","[3][1][0]","[3][1][1]","[3][1][2]","[5][1][0]"],
            ["[4][2][2]","[3][2][0]","[3][2][1]","[3][2][2]","[5][2][0]"],
            ["","[1][0][0]","[1][0][1]","[1][0][2]",""]]

left_face = [["","[0][0][0]","[0][1][0]","[0][2][0]",""],
            ["[2][0][2]","[4][0][0]","[4][0][1]","[4][0][2]","[3][0][0]"],
            ["[2][1][2]","[4][1][0]","[4][1][1]","[4][1][2]","[3][1][0]"],
            ["[2][2][2]","[4][2][0]","[4][2][1]","[4][2][2]","[3][2][0]"],
            ["","[1][2][0]","[1][1][0]","[1][0][0]",""]]

right_face = [["","[0][2][2]","[0][1][2]","[0][0][2]",""],
            ["[3][0][2]","[5][0][0]","[5][0][1]","[5][0][2]","[2][0][0]"],
            ["[3][1][2]","[5][1][0]","[5][1][1]","[5][1][2]","[2][1][0]"],
            ["[3][2][2]","[5][2][0]","[5][2][1]","[5][2][2]","[2][2][0]"],
            ["","[1][0][2]","[1][1][2]","[1][2][2]",""]]

def side_select(side):
    side = side.lower()
    return (eval(side+"_face"))
