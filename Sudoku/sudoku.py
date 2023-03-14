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
# 
root.geometry("700x500")
# => Fonction pour changer longeur/largeur de la fênetre trouvé après recherches sur
####### https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter
Sudoku_Canvas = Canvas(root, width= Canvas_Width, height= Canvas_Height)

###### Création du dictionnaire du jeu 
###### + liste des nombres qui ne peuvent pas êtres changés

Sudoku_Dict = {}
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
print(Sudoku_Dict)

Sudoku_RigidNumbers = []

##### 
#####

######################### FIN DU PROGRAMME
root.mainloop()