############# SUDOKU #############
###        Oliwier Szmyt       ###  
###         Azzi Aicha         ###  
###          Joey Zhan         ###
###         Sirmen Reka        ###
##################################
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from tkinter import *
import random
import webbrowser

global Canvas_Height
global Canvas_Width
Canvas_Width = 600
Canvas_Height = 600
Canvas_Padding = 100
Background_Color = "#CCCCCC"
ThickLine_Color = "white"
Line_Color = "gray"
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
###### Initialisation du tableau du jeu

root = Tk()
root.title("SUDOKU")
root.geometry("600x600")

Sudoku_Canvas = Canvas(root,bg=Background_Color, width= Canvas_Width, height= Canvas_Height)
Sudoku_Canvas.grid(column=Canvas_Padding,row=Canvas_Padding,columnspan=20,rowspan=20)

#boucle for pour dessiner les lignes et les colonnes de la grille
for i in range(10):
    if i % 3 == 0:
        width = 2
    else:
        width = 1
    # ligne verticale
    Sudoku_Canvas.create_line((i/9)*Canvas_Width, 0, (i/9)*Canvas_Width, Canvas_Height, width=width, fill=Line_Color)
    # ligne horizontale
    Sudoku_Canvas.create_line(0, (i/9)*Canvas_Height, Canvas_Width, (i/9)*Canvas_Height, width=width, fill=Line_Color)

#boucle for pour dessiner les regions
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        x1, y1 = (j/9)*Canvas_Width, (i/9)*Canvas_Height
        x2, y2 = ((j+3)/9)*Canvas_Width, ((i+3)/9)*Canvas_Height
        Sudoku_Canvas.create_rectangle(x1, y1, x2, y2, width=6,fill='gray80', outline=ThickLine_Color)

#boucle for pour dessiner les rectangles
for i in range(0, 9):
    for j in range(0, 9):
        x1, y1 = (j/9)*Canvas_Width, (i/9)*Canvas_Height
        x2, y2 = ((j+1)/9)*Canvas_Width, ((i+1)/9)*Canvas_Height
        Sudoku_Canvas.create_rectangle(x1, y1, x2, y2, width=1, outline=Line_Color)
        #ajouter une zone de texte à chaque rectangle
        #cell = Entry(Sudoku_Canvas, width=3, font=("Helvetica", 20))
        #Sudoku_Canvas.create_window((x1+x2)//2, (y1+y2)//2, window=cell)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Sudoku_Dict = {}
# ---> Dictionnaire contenant les cellules de Sudoku en clés (de gauche à droite, de haut en bas)
# ---> et les valeurs étant le nombre contenus dans ces cellules.
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
print(Sudoku_Dict)
#
Sudoku_RigidNumbers = []
# ---> Liste / tableau contenant les cases ( ex: 20,51,3 ) qui ne pourront pas être changés au milieu
# ---> de la partie.

def choose_difficulty_easy(facile):
    facile = random.choice(grille_facile)

boutton_difficulte_facile = Button(root,command=choose_difficulty_easy,text="Facile",bd=5,font = ("helvetica", "30"),padx=5, pady=5, bg="cyan")

#Difficulter facile
grille_facile = [[0, 5, 0, 0, 2, 0, 9, 0, 0], [0, 7, 0, 0, 5, 6, 1, 0, 0], [0, 3, 0, 1, 8, 7, 0, 2, 0],
                 [0, 0, 0, 9, 0, 0, 0, 1, 5], [0, 4, 5, 0, 0, 0, 2, 9, 0], [4, 8, 0, 0, 0, 2, 0, 0, 0],
                 [0, 9, 0, 5, 1, 4, 0, 3, 0], [0, 0, 3, 2, 4, 0, 0, 8, 0], [0, 0, 2, 0, 3, 0, 0, 7, 0]]

grille_facile2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_facile3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_facile4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_facile5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#Diff Moyen
grille_moyen =[[0, 0, 0, 0, 0, 9, 0, 0, 0], [5, 6, 8, 0, 1, 0, 4, 0, 0], [0, 0, 6, 0, 4, 0, 0, 7, 1],
                 [2, 0, 0, 0, 3, 8, 0, 0, 0], [0, 0, 2, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 2, 5, 0],
                 [7, 3, 4, 0, 0, 0, 5, 9, 0], [1, 9, 7, 0, 0, 0, 0, 0, 0], [8, 0, 0, 7, 2, 0, 3, 0, 0]]

grille_moyen2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_moyen3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_moyen4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_moyen5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


#Difficulter difficile
grille_difficile =[[0, 5, 8, 0, 0, 0, 0, 0, 0], [0, 6, 0, 0, 0, 0, 0, 3, 0], [0, 9, 6, 3, 0, 0, 0, 7, 0],
                   [0, 0, 2, 0, 8, 7, 9, 0, 0], [3, 0, 0, 0, 6, 0, 5, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 9],
                   [0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 5, 0, 8, 7, 0, 4], [0, 0, 0, 8, 0, 0, 2, 5, 0]]

grille_difficile2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_difficile3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_difficile4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille_difficile5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


#Fonction qui vérifie si la valeur est comprise entre 0 et 9 uniquement
def verifie_case(widget_verification, valeur):
    if valeur.isdigit() and int(valeur) in range(10):
        # Définition de la valeur de la case
        widget_verification.config(bg="grey")
        label = root.Label(widget_verification, text=valeur)
        label.pack()
    else:
        widget_verification.config(bg="red")
        label = root.Label(widget_verification, text="Erreur")
        label.pack()

#Fonction qui permet de cliquer pour ensuite mettre un nombre de 0 à 9
def click_case(event):
    widget = event.widget
    x = widget.grid_info()['row']
    y = widget.grid_info()['column']

    input_window = root.Toplevel()
    input_window.title("Champs de saisie (valeur entre 0 et 9): ")
    input_window.geometry("400x70")

    input_entry = root.Entry(input_window, width=5)
    input_entry.pack(pady=10)
    submit_button = root.Button(input_window, text="Valider Valeur", command=lambda: verifie_case(widget, input_entry.get()))
    submit_button.pack()

#Barre de menu
barre_de_menus = Menu(root)
 #menus difficultée
menu_grille = Menu(barre_de_menus, tearoff=0)
barre_de_menus.add_cascade(label="Choix Difficultée", menu=menu_grille)
menu_grille.add_command(label="Grille Facile", command=grille_facile)
menu_grille.add_command(label="Grille Moyen", command=grille_moyen)
menu_grille.add_command(label="Grille Difficile", command=grille_difficile)
menu_grille.add_separator()
menu_grille.add_command(label="Exit", command=root.quit)
    #menus aide
def ouvrir_lien_regles():
    webbrowser.open('https://sudoku.com/fr/comment-jouer/regles-de-sudoku-pour-les-debutants-complets/')

menu_aide = Menu(barre_de_menus, tearoff=0)
barre_de_menus.add_cascade(label="Aide", menu=menu_aide)
menu_aide.add_command(label="Regle du Sudoku",command=ouvrir_lien_regles)

root.config(menu=barre_de_menus)
root.mainloop()
#fin du code