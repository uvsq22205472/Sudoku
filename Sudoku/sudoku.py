                ############# SUDOKU #############
                ###         Sirmen Reka        ###  
                ###          Joey Zhan         ###  
                ###          Azzi Aicha        ###
                ###         Oliwier Szmyt      ###
                ##################################
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Valeurs Definition=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from tkinter import *
from tkinter import messagebox
from random import randint
import random
import webbrowser

global Canvas_Height
global Canvas_Width
Canvas_Width = 600
Canvas_Height = 600

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Initialisation du tableau du jeu-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

root = Tk()
root.title("SUDOKU")
root.geometry("750x600")

Sudoku_Canvas = Canvas(root,bg='#CCCCCC', width= Canvas_Width, height= Canvas_Height)
Sudoku_Canvas.grid(column=0,row=0,columnspan=20,rowspan=20)
Sudoku_liste_valeurs = [[0 for j in range(9)] for i in range(9)]


#----------------------------------------------Entrer valeur---------------------------------------------------------



#Fonction qui permet de cliquer pour ensuite mettre un chiffre de 1 à 9
def on_click(event):
    return None


def fenetre_input_valeur(event):
    #Position du clic
    x, y = event.x, event.y
    #Calculer la position de la case par rapport au clic
    col = int(x // (Canvas_Width / 9))
    row = int(y // (Canvas_Height / 9))
    #Fenetre
    input_window = Toplevel(root)
    input_window.title("Champs de saisie")
    # --> https://datatofish.com/entry-box-tkinter/
    # --> https://stackoverflow.com/questions/42211865/how-to-add-text-to-a-toplevel-window
    InputWindowText = "\nVeuillez entrer une valeur comprise entre 1 et 9 puis Valider\nou cliquer sur Effacer pour effacer la valeur dans la case."
    Label(input_window, text=InputWindowText).pack()
    # -- -- --
    input_window.geometry("330x160")

    #Champs de saisie
    entry = Entry(input_window)
    entry.pack(pady=10)

    #Placer dans la case du sudoku
    def placer_valeur():
        """ docstring

        """
        CurrentCellTag = "Cell"+str(row)+";"+str(col)
        value = entry.get()
        if value.isnumeric() == True and 1<=int(value)<=9:
            value = int(value)
            Sudoku_liste_valeurs[row][col] = value
            #pour placer le texte + au milieux de la case (1/18)
            x1 = (col/9)*Canvas_Width + (Canvas_Width/18)
            y1 = (row/9)*Canvas_Height + (Canvas_Height/18)
            current_item = Sudoku_Canvas.find_withtag(CURRENT)
            texte = Sudoku_Canvas.delete(CurrentCellTag)
            texte = Sudoku_Canvas.create_text(x1, y1, text=value, font=("Helvetica", 16),tag=CurrentCellTag)
            Sudoku_Canvas.itemconfig(current_item, text=texte)
            print(Sudoku_liste_valeurs)
        elif value == "":
            erase_value()
            # Si rien est entre dans, alors cela suprime la valeur dans la case et met 0 ou "rien" dans le tableau.
        else:
            messagebox.showerror(title="Erreur",message="Veuillez à entrer un nombre compris entre 1 et 9.")
        input_window.destroy()
    def erase_value():
        CurrentCellTag = "Cell"+str(row)+";"+str(col)
        Sudoku_liste_valeurs[row][col]= 0
        texte = Sudoku_Canvas.delete(CurrentCellTag)
        input_window.destroy()
        return None
    #creation d'un bouton pour valider la saisie et placer la valeur dans la case du sudoku
    button = Button(input_window, text="Valider", command=placer_valeur)
    button.pack()

    erase_button = Button(input_window,text="Effacer", command=erase_value)
    erase_button.pack()

#----------------------------------------------Géneration aléatoire de tableau ---------------------------------------------------------
# Generation du tableau completement aleatoire
def RandomBoard(board):
    RandomCellsRemaining = randint(25,35)

# Chaque sous-liste est une région, notée de cette façon.
# 1  2  3
# 4  5  6
# 7  8  9
Sudoku_RigidCells = []
# Liste des *cases* ( de 1 a 81 ) qui ne peuvent pas etres modifiees





#Sudoku_Dict = {}
# ---> Dictionnaire contenant les cellules de Sudoku en clés (de gauche à droite, de haut en bas)
# ---> et les valeurs étant le nombre contenus dans ces cellules.
#for CellNumber in range(1,82):
#    Sudoku_Dict[("Cell_"+str(CellNumber))] = "X"
#print(Sudoku_Dict)
#
#Sudoku_RigidNumbers = []
# ---> Liste / tableau contenant les cases ( ex: 20,51,3 ) qui ne pourront pas être changés au milieu
# ---> de la partie.

#ButtonText = str()
#for vertical in range(0,9):
#    horizontal = 0
#    for horizontal in range(0,9):
#        Sudoku_Button = Button(root,text=(str(horizontal+1)+","+str(vertical+1)), font=("helvetica", "12"), relief="groove")
#        Sudoku_Button.grid(column=vertical,row=horizontal)
#        Sudoku_Button["command"] = lambda Sudoku_Button = Sudoku_Button: click_case(Sudoku_Button)
#        # --- > https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments
#        # --- > Utilisation de la reponse de l'utilisateur "Joel" de StackOverflow.

#----------------------------------------------Timer-----------------------------------------------------------------

timer_en_marche = False
minutes = 0
secondes = 0
'''Modifie ici pour que ca commence quand tu met le module aleatoire'''

def demarrer_timer():
    global timer_en_marche
    if not timer_en_marche:
        timer()
        timer_en_marche = True

def timer():
    global minutes, secondes
    secondes = secondes + 1
    ecriture_minutes = f'{minutes}' if minutes > 9 else f'0{minutes}'
    ecriture_secondes = f'{secondes}' if secondes > 9 else f'0{secondes}'
    timer_ecriture.config(text=ecriture_minutes + ':' + ecriture_secondes)
    if secondes == 60:
        minutes = minutes + 1
        secondes = 0
    global maj_timer
    maj_timer = timer_ecriture.after(1000, timer)


timer_ecriture = Label(font=('Helvetica', 30), text='00:00')
timer_ecriture.place(x=620, y=10)

start_button = Button(text='Débuter', height=1, width=8, font=('Helvetica', 22), command=demarrer_timer)
start_button.place(x=605, y=80)
#----------------------------------------------Dessin Graphique---------------------------------------------------------


#boucle for pour dessiner les rectangles
for i in range(0, 9):
    for j in range(0, 9):
        x1, y1 = (j/9)*Canvas_Width, (i/9)*Canvas_Height
        x2, y2 = ((j+1)/9)*Canvas_Width, ((i+1)/9)*Canvas_Height
        Rectangle = Sudoku_Canvas.create_rectangle(x1, y1, x2, y2, width=1, outline='gray',fill="gray90")
        Sudoku_Canvas.tag_bind(Rectangle, '<Button-1>', fenetre_input_valeur)
        Sudoku_Canvas.grid(row=i, column=j)
#boucle for pour dessiner les regions
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        x1, y1 = (j/9)*Canvas_Width, (i/9)*Canvas_Height
        x2, y2 = ((j+3)/9)*Canvas_Width, ((i+3)/9)*Canvas_Height
        Sudoku_Canvas.create_rectangle(x1, y1, x2, y2, width=3)
        Sudoku_Canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, width=4, outline="white")


#------------------------------------------------Difficultée---------------------------------------------------------


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


#---------------------------------------------------MENU-------------------------------------------------------------

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

#------------------------------------------------------FIN------------------------------------------------------------
root.mainloop()
#fin du code