from tkinter import *
import random
import webbrowser

global Canvas_Height
global Canvas_Width
Canvas_Width = 500
Canvas_Height = 500

root = Tk()
root.title("SUDOKU")
root.geometry("800x600")
Sudoku_Canvas = Canvas(root, width= Canvas_Width, height= Canvas_Height)

Sudoku_Dict = {}
for CellNumber in range(1,82):
    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
print(Sudoku_Dict)

Sudoku_RigidNumbers = []

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

Region1 = Button(root,text=Sudoku_Dict["Cell_1"],)
Region1.grid(row=1,column=1)

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