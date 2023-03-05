############# SUDOKU #############
###          Crée par:         ###
###        SZMYT Oliwier       ###
###        -------------       ###
###        -------------       ###
###        -------------       ###
##################################

from tkinter import *
from random import randint

############[Tunable]############
global Canvas_Height
global Canvas_Width
Canvas_Width = 500
Canvas_Height = 500
#################################

# Initialisation du tableau du jeu
root = Tk()
root.title("SUDOKU")
Sudoku_Canvas = Canvas(root, width= Canvas_Width, height= Canvas_Height)

