############# SUDOKU #############
###          Crée par:         ###
###  (RP)  Oliwier Szmyt       ###
###  (QC)   Azzi Aicha         ###
###          Joey Zhan         ###
###         Sirmen Reka        ###
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

Background_Color = "#CCCCCC"
ThickLine_Color = "white"
Line_Color = "gray"
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Initialisation du tableau du jeu
root = Tk()
root.title("SUDOKU")
root.geometry("800x600")
# => Fonction pour changer longeur/largeur de la fênetre trouvé après recherches sur
####### https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter

# Lignes
Sudoku_Canvas = Canvas(root,bg=Background_Color, width= Canvas_Width, height= Canvas_Height)
Sudoku_Canvas.grid(column=Canvas_Padding,row=Canvas_Padding,columnspan=20,rowspan=20)



# le code en bas fonctionne mais c'est pas joli, il faudra faire une triple boucle for 
for i in range(9):
    Sudoku_Canvas.create_line((200/3)*i,0,(200/3)*i,600,width=1, fill=Line_Color)
for i in range(9):
    Sudoku_Canvas.create_line(0,(200/3)*i,600,(200/3)*i,width=1,fill=Line_Color)

Sudoku_Canvas.create_rectangle((0,0),(200,200),width=2,outline=ThickLine_Color)
Sudoku_Canvas.create_rectangle((0,200),(200,400),width=2,outline=ThickLine_Color)
Sudoku_Canvas.create_rectangle((0,400),(200,600),width=2,outline=ThickLine_Color)

Sudoku_Canvas.create_rectangle((200,0),(400,200),width=2,outline=ThickLine_Color)
Sudoku_Canvas.create_rectangle((200,200),(400,400),width=2,outline=ThickLine_Color)
Sudoku_Canvas.create_rectangle((200,400),(400,600),width=2,outline=ThickLine_Color)

Sudoku_Canvas.create_rectangle((400,0),(600,200),width=2,outline=ThickLine_Color)
Sudoku_Canvas.create_rectangle((400,200),(600,400),width=2,outline=ThickLine_Color)
Sudoku_Canvas.create_rectangle((400,400),(600,600),width=2,outline=ThickLine_Color)
#
#Sudoku_Canvas.create_line((200/3),0,(200/3),600,width=1,fill=Line_Color)
#for Column in range(0,10):
    #for Row in range(0,10):
        #Sudoku_Canvas.create_rectangle((0+((Column-1)*(200/3)),(0+((Row-1)*(200/3))),(200+((Column-1)*(200/3)),(0+((Row-1)*(200/3))))),width=1,outline=Line_Color)






#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Sudoku_Dict = {}
# ---> Dictionnaire contenant les cellules de Sudoku en clés (de gauche à droite, de haut en bas)
# ---> et les valeurs étant le nombre contenus dans ces cellules.
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
print(Sudoku_Dict)
#Creation de 
Sudoku_RigidNumbers = []
# ---> Liste / Tableau des nombres de cases ( ex: 11, 20, 69 ) des nombres qui ne pourront pas 
# ---> être changés lors d'une partie.



#Region1 = Button(root,text=Sudoku_Dict["Cell_1"],)
#Region1.grid(row=1,column=1)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##### 
#####
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
######################### FIN DU PROGRAMME
root.mainloop()