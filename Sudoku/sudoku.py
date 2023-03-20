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
#def Create81Buttons(Board_Root):


        
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Canvas_Width = 600
Canvas_Height = 600
Canvas_Padding = 20

ThickLine_Color = "white"
Line_Color = "gray"
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Initialisation du tableau du jeu
root = Tk()
root.title("SUDOKuU")
root.geometry("800x600")
# => Fonction pour changer longeur/largeur de la fênetre trouvé après recherches sur
####### https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter

# Il y a une maniere plus interessante de faire ca avec une triple boucle for.





Sudoku_Canvas = Canvas(root,bg="pink", width= Canvas_Width, height= Canvas_Height)
Sudoku_Canvas.grid(column=Canvas_Padding,row=Canvas_Padding,columnspan=20,rowspan=20)


for Y in range(0,4):
    for X in range(0,4):
        Sudoku_Canvas.create_rectangle((((Y-1)*200),((X-1)*200))

#Sudoku_Canvas.create_rectangle((0,0),(200,200),width=2,outline=ThickLine_Color)
#Sudoku_Canvas.create_rectangle((0,200),(200,400),width=2,outline=ThickLine_Color)
#Sudoku_Canvas.create_rectangle((0,400),(200,600),width=2,outline=ThickLine_Color)

#Sudoku_Canvas.create_rectangle((200,0),(400,200),width=2,outline=ThickLine_Color)
#Sudoku_Canvas.create_rectangle((200,200),(400,400),width=2,outline=ThickLine_Color)
#Sudoku_Canvas.create_rectangle((200,400),(400,600),width=2,outline=ThickLine_Color)

#Sudoku_Canvas.create_rectangle((400,0),(600,200),width=2,outline=ThickLine_Color)
#Sudoku_Canvas.create_rectangle((400,200),(600,400),width=2,outline=ThickLine_Color)
#Sudoku_Canvas.create_rectangle((400,400),(600,600),width=2,outline=ThickLine_Color)
#





#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Création du dictionnaire du jeu 
###### + liste des nombres qui ne peuvent pas êtres changés

Sudoku_Dict = {}
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
#print(Sudoku_Dict)
#Creation de 

Sudoku_RigidNumbers = []
# Liste des nombres qui ne peuvent pas etre changes.



#Region1 = Button(root,text=Sudoku_Dict["Cell_1"],)
#Region1.grid(row=1,column=1)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##### 
#####
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
######################### FIN DU PROGRAMME
root.mainloop()