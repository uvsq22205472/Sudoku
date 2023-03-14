############# SUDOKU #############
###          Crée par:         ###
###        SZMYT Oliwier       ###
###        -------------       ###
###        -------------       ###
###        -------------       ###
##################################

from tkinter import *
from random import randint

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
global Canvas_Height
global Canvas_Width
Canvas_Width = 500
Canvas_Height = 500
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Initialisation du tableau du jeu
root = Tk()
root.title("SUDOKU")
Sudoku_Canvas = Canvas(root, width= Canvas_Width, height= Canvas_Height)
Sudoku_Canvas


###### Création du dictionnaire du jeu 
###### + liste des nombres qui ne peuvent pas êtres changés

Sudoku_Dict = {}
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = None
print(Sudoku_Dict)

Sudoku_RigidNumbers = []

##### 
#####






######################### FIN DU PROGRAMME
root.mainloop()