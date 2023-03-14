############# SUDOKU #############
###          Crée par:         ###
###  (RP)  SZMYT Oliwier       ###
###        -------------       ###
###        -------------       ###
###        -------------       ###
##################################
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from tkinter import *
from random import randint
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
### Fonctions 
def InitializeBoard(Board_Root):
    """docstring pour aicha

    Input:

    Output:
    """
    return None
def Create81Buttons(Board_Root):
    """
    """
    for vertical_iteration
    for horizontal_iteration in range(1,4):
        ("Region" + str(iteration) = Button(root,text=Sudoku_Dict["Cell_" + str(iteration)],))
        ("Region" + str(iteration).grid(row=1),column=()))



#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
global Canvas_Height
global Canvas_Width
Canvas_Width = 500
Canvas_Height = 500
#test
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Initialisation du tableau du jeu
root = Tk()
root.title("SUDOKU")
root.geometry("800x600")
# => Fonction pour changer longeur/largeur de la fênetre trouvé après recherches sur
####### https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter
Sudoku_Canvas = Canvas(root, width= Canvas_Width, height= Canvas_Height)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Création du dictionnaire du jeu 
###### + liste des nombres qui ne peuvent pas êtres changés

Sudoku_Dict = {}
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
#print(Sudoku_Dict)

Sudoku_RigidNumbers = []
#test



#Region1 = Button(root,text=Sudoku_Dict["Cell_1"],)
#Region1.grid(row=1,column=1)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##### 
#####
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
######################### FIN DU PROGRAMME
root.mainloop()