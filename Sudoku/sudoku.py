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
import pickle

global Canvas_Height
global Canvas_Width

global Sudoku_liste_valeurs
Sudoku_liste_valeurs = [[0 for i in range(9)] for j in range(9)]
global Sudoku_Rigid_Cells
Sudoku_Rigid_Cells = [[0 for i in range(9)] for j in range(9)]

Canvas_Width = 600
Canvas_Height = 600

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Initialisation du tableau du jeu-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

root = Tk()
root.title("SUDOKU")
root.geometry("750x600")

Sudoku_Canvas = Canvas(root,bg='#CCCCCC', width= Canvas_Width, height= Canvas_Height)
Sudoku_Canvas.grid(column=0,row=0,columnspan=20,rowspan=20)


#----------------------------------------------Entrer valeur---------------------------------------------------------



#Fonction qui permet de cliquer pour ensuite mettre un chiffre de 1 à 9

def fenetre_input_valeur(event):
    #Position du clic
    x, y = event.x, event.y
    #Calculer la position de la case par rapport au clic
    col = int(x // (Canvas_Width / 9))
    row = int(y // (Canvas_Height / 9))
    print("ROW / COL :",row,col)
    print("LIST :",Sudoku_liste_valeurs)
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
        CurrentCellTag = "Cellule"+str(row)+";"+str(col)
        value = entry.get() 
        if value.isnumeric() == True and 1<=int(value)<=9:
            value = int(value)
            if VerifContraintes(row,col, value) == True:
                #pour placer le texte + au milieux de la case (1/18)
                Sudoku_liste_valeurs[row][col] = value
                x1 = (col/9)*Canvas_Width + (Canvas_Width/18)
                y1 = (row/9)*Canvas_Height + (Canvas_Height/18)
                current_item = Sudoku_Canvas.find_withtag(CURRENT)
                texte = Sudoku_Canvas.delete(CurrentCellTag)
                texte = Sudoku_Canvas.create_text(x1, y1, text=value, font=("Helvetica", 16),tag=CurrentCellTag)
                Sudoku_Canvas.itemconfig(current_item, text=texte)
                print(Sudoku_liste_valeurs)
            else:
                messagebox.showerror(title="Erreur",message="Verifiez que votre nombre n'est pas présent déjà sur la ligne, colonne et région.")
        elif value == "":
            erase_value()
            # Si rien est entre dans, alors cela suprime la valeur dans la case et met 0 ou "rien" dans le tableau.
        else:
            messagebox.showerror(title="Erreur",message="Veuillez à entrer un nombre compris entre 1 et 9.")
        input_window.destroy()
        Sudoku_Update()
    def erase_value():
        CurrentCellTag = "Cellule"+str(row)+";"+str(col)
        Sudoku_liste_valeurs[row][col]= 0
        texte = Sudoku_Canvas.delete(CurrentCellTag)
        input_window.destroy()
        Sudoku_Update()
        return None
    #creation d'un bouton pour valider la saisie et placer la valeur dans la case du sudoku
    button = Button(input_window, text="Valider", command=placer_valeur)
    button.pack()

    erase_button = Button(input_window,text="Effacer", command=erase_value)
    erase_button.pack()
def VerifContraintes(row, col, num):
    # Verif pour les lignes
    if num in Sudoku_liste_valeurs[row]:
        return False
    # Verif pour les colonnes
    for i in range(len(Sudoku_liste_valeurs)):
        if Sudoku_liste_valeurs[i][col] == num:
            return False
    # Verif pour le carree
    SquareRow = (row // 3) * 3
    SquareCol = (col // 3) * 3
    for i in range(SquareRow, SquareCol + 3):
        for j in range(SquareRow, SquareCol + 3):
            if Sudoku_liste_valeurs[i][j] == Sudoku_liste_valeurs:
                return False

    return True

#----------------------------------------------Géneration aléatoire de tableau ---------------------------------------------------------
# Generation du tableau completement aleatoire
def Sudoku_GenerateBoard(difficulty: str):
    """Input : difficulty (str) = Difficulté choisie par l'utiliseur
    Output : board (list) = Tableau de Sudoku utilisé par le jeu

    Cette fonction génére un tableau de jeu de Sudoku complete avant de le vider selon la difficulté choisi.
    La difficulté influence le nombre des cases à vider, puis cette fonction renvoie le tableau et met à jour le tableau pour
    l'afficher.
    
    """
    global Sudoku_liste_valeurs
    Sudoku_FillBoard(Sudoku_liste_valeurs)
    Sudoku_UnfillBoard(Sudoku_liste_valeurs, difficulty)
    print(Sudoku_liste_valeurs)
    Sudoku_Update()
    return Sudoku_liste_valeurs

def Sudoku_FillBoard(board: list):
    if not EmptyCellCheck(board):
        return True
    
    row, col = EmptyCellCheck(board)
    values = list(range(1, 10))
    random.shuffle(values)
    
    for val in values:
        if ValidCellCheck(board, row, col, val):
            board[row][col] = val
            
            if Sudoku_FillBoard(board):
                return True
            
            board[row][col] = 0
            
    return False

def EmptyCellCheck(board: list):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def ValidCellCheck(board: list, row: int, col: int, val: int):
    for i in range(9):
        if board[row][i] == val or board[i][col] == val:
            return False
        
    r = row - row % 3
    c = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j] == val:
                return False
    return True

def Sudoku_UnfillBoard(board: list, difficulty: str):
    if difficulty == 'easy':
        CellsToRemove = randint(35, 45)
    elif difficulty == 'medium':
        CellsToRemove = randint(46, 55)
    elif difficulty == 'hard':
        CellsToRemove = randint(56, 65)
    else:
        print("Erreur: difficulté n'est pas disponible")
        return False
    
    for i in range(CellsToRemove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0
    return True
#----------------------------------------------Difficulte------------------------------------------------------------
def Sudoku_Update():
    global Sudoku_liste_valeurs
    #print("ENTRY",Sudoku_liste_valeurs)
    row , col = 0, 0
    for row in range(9):
        for col in range(9):
            CurrentCellTag = "Cellule"+str(row)+";"+str(col)
            x1 , y1 = (col/9)*Canvas_Width + (Canvas_Width/18) , (row/9)*Canvas_Height + (Canvas_Height/18)
            current_item = Sudoku_Canvas.find_withtag(CURRENT)
            texte = Sudoku_Canvas.delete(CurrentCellTag)
            if Sudoku_liste_valeurs[row][col] != 0:
                texte = Sudoku_Canvas.create_text(x1, y1, text=Sudoku_liste_valeurs[row][col], font=("Helvetica", 16),tag=CurrentCellTag)
            else:
                texte = Sudoku_Canvas.create_text(x1, y1, text="", font=("Helvetica", 16),tag=CurrentCellTag)
            Sudoku_Canvas.itemconfig(current_item, text=texte)
    #print("LAST",Sudoku_liste_valeurs)
    FinishCheck()
    return Sudoku_liste_valeurs
     
def StartGame(difficulty: str):
    global Sudoku_liste_valeurs
    global minutes , secondes

    if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
        Sudoku_liste_valeurs = [[0 for i in range(9)] for j in range(9)]
        Sudoku_liste_valeurs = Sudoku_GenerateBoard(difficulty)
        Sudoku_Rigid_Cells =  Sudoku_liste_valeurs
    else:
        Grilles_generes_auparavant(difficulty)
# Mettre redemarrer timer
    if not timer_en_marche:
        demarrer_timer()
    else:
        redemarrer_timer()
    Sudoku_Update()
    DifficultyWindow.destroy()
    return Sudoku_liste_valeurs


def StartWindow():
    global DifficultyWindow
    DifficultyWindow = Toplevel()
    DifficultyWindow.title("Choix de la difficulté")
    DifficultyText = "Choissisez une grille aleatoire ou pre-généré"
    DifficultyWindow.geometry("490x100")
    Label(DifficultyWindow, text=DifficultyText).grid(column=1)
    EasyBut = Button(DifficultyWindow,fg='green' ,text="Aléatoire : Facile", command=lambda: StartGame("easy"))
    EasyBut.grid(column=0,row=4,padx=15)

    MedBut = Button(DifficultyWindow,fg='orange', text="Aléatoire : Moyen", command=lambda: StartGame("medium"))
    MedBut.grid(column=0,row=6)

    HardBut = Button(DifficultyWindow,fg='red' ,text="Aléatoire : Difficile", command=lambda: StartGame("hard"))
    HardBut.grid(column=0,row=8)

    EasyButPreRemp = Button(DifficultyWindow, fg='green',text="Pré-généré : Facile", command=lambda: StartGame("facile"))
    EasyButPreRemp.grid(column=4,row=4)

    MedButPreRemp = Button(DifficultyWindow,fg='orange' ,text="Pré-généré : Moyen", command=lambda: StartGame("moyen"))
    MedButPreRemp.grid(column=4,row=6)

    HardButPreRemp = Button(DifficultyWindow,fg='red' ,text="Pré-généré : Difficile", command=lambda: StartGame("difficile"))
    HardButPreRemp.grid(column=4,row=8)
    DifficultyWindow.mainloop()

def Grilles_generes_auparavant (difficulty: str):
    global Sudoku_liste_valeurs

    if difficulty == "facile":
        Sudoku_liste_valeurs = [
            [0, 0, 4, 0, 5, 0, 0, 0, 6],
            [6, 0, 0, 2, 0, 0, 0, 9, 0],
            [0, 0, 5, 0, 6, 0, 2, 0, 0],
            [3, 0, 0, 0, 0, 8, 0, 0, 9],
            [0, 8, 0, 0, 0, 0, 0, 7, 0],
            [5, 0, 0, 7, 0, 0, 0, 0, 2],
            [0, 0, 9, 0, 7, 0, 3, 0, 0],
            [0, 3, 0, 0, 0, 1, 0, 0, 7],
            [1, 0, 0, 0, 9, 0, 8, 0, 0]
        ]
        print(Sudoku_liste_valeurs)
    elif difficulty == "moyen":
        Sudoku_liste_valeurs = [
            [0, 0, 6, 7, 0, 0, 0, 4, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 3, 4, 0, 0, 1, 0, 8],
            [0, 0, 0, 0, 8, 0, 5, 0, 0],
            [8, 0, 0, 0, 3, 0, 0, 0, 2],
            [0, 0, 5, 0, 9, 0, 0, 0, 0],
            [5, 0, 8, 0, 0, 6, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 0, 8, 4, 0, 0]
        ]
        print(Sudoku_liste_valeurs)
    elif difficulty == "difficile":
        Sudoku_liste_valeurs = [
            [0, 9, 0, 0, 0, 5, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 8, 2, 0, 3, 0, 6, 0],
            [0, 0, 0, 0, 9, 0, 0, 0, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 4, 6, 0, 8, 0, 3, 0],
            [0, 0, 2, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 9, 0],
            [1, 0, 0, 9, 0, 2, 0, 0, 3]
        ]
        print(Sudoku_liste_valeurs)
    else:
        print("Difficulté non valide")
        return None
    return Sudoku_liste_valeurs


#----------------------------------------------Timer-----------------------------------------------------------------

timer_en_marche = False
minutes = 0
secondes = 0
''''''

def demarrer_timer():
    global timer_en_marche
    if not timer_en_marche:
        timer_en_marche = True
        timer()

def eteindre_timer():
    global timer_en_marche
    if timer_en_marche:
        timer_en_marche = False
        timer_ecriture.after_cancel(maj_timer)
        minutes = 0
        secondes = 0
        timer()

def redemarrer_timer():
    global timer_en_marche
    if timer_en_marche:
        eteindre_timer()
        demarrer_timer()

def timer():
    if timer_en_marche == True:
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
    else:
        minutes = 0
        secondes = 0

timer_ecriture = Label(font=('Helvetica', 30), text='00:00')
timer_ecriture.place(x=620, y=10)

start_button = Button(text='Débuter', height=1, width=8, font=('Helvetica', 22), command=StartWindow)
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

#------------------------------------------------MENU-------------------------------------------------------------

#Barre de menu
barre_de_menus = Menu(root)
 #menus difficultée
menu_grille = Menu(barre_de_menus, tearoff=0)
#barre_de_menus.add_cascade(label="Choix Difficultée", menu=menu_grille)
#menu_grille.add_command(label="Grille Facile", command=Sudoku_GenerateBoard("easy"))
#menu_grille.add_command(label="Grille Moyen", command=Sudoku_GenerateBoard("medium"))
#menu_grille.add_command(label="Grille Difficile", command=Sudoku_GenerateBoard("hard"))
#menu_grille.add_separator()
#menu_grille.add_command(label="Exit", command=root.quit)
    #menus aide
def ouvrir_lien_regles():
    webbrowser.open('https://sudoku.com/fr/comment-jouer/regles-de-sudoku-pour-les-debutants-complets/')

menu_aide = Menu(barre_de_menus, tearoff=0)
barre_de_menus.add_cascade(label="Aide", menu=menu_aide)
menu_aide.add_command(label="Regle du Sudoku",command=ouvrir_lien_regles)

root.config(menu=barre_de_menus)
#------------------------------------------------------Annuler------------------------------------------------------------
"""fonction pour quitter, efface tout"""
def annuler_partie():
    global Sudoku_liste_valeurs
    global Sudoku_Rigid_Cells
    Sudoku_Rigid_Cells = [[0 for i in range(9)] for j in range(9)]
    Sudoku_liste_valeurs = [[0 for i in range(9)] for j in range(9)]
    eteindre_timer()
    Sudoku_Update()
    print(Sudoku_liste_valeurs)
    return Sudoku_liste_valeurs, Sudoku_Rigid_Cells

annuler_button = Button(root, text="Annuler la partie", command=annuler_partie)
annuler_button.place(x=605, y=220)

#------------------------------------------------------Sauvegarde------------------------------------------------------------
#https://www.quennec.fr/trucs-astuces/langages/python/python-le-module-pickle
#On a mis en dictionnaire pour pas refaire 3x la meme fonction

sauvegardes = {
    'sauvegarde 1': 'sudoku.grille',
    'sauvegarde 2': 'sudoku.grille2',
    'sauvegarde 3': 'sudoku.grille3'
}

charges = {
    'charge 1': 'sudoku.grille',
    'charge 2': 'sudoku.grille2',
    'charge 3': 'sudoku.grille3'
}

def liste_sauvegarde():
    sauvegarde_window = Toplevel(root)
    sauvegarde_window.title("Champs de saisie")
    InputWindowText = "Fenetre de sauvegarde"
    Label(sauvegarde_window, text=InputWindowText).pack()
    sauvegarde_window.geometry("330x120")
    for sauvegarde, fichier in sauvegardes.items():
        Button(sauvegarde_window, text=sauvegarde, command=lambda f=fichier: sauvegarder(f)).pack()

def liste_charger():
    sauvegarde_window = Toplevel(root)
    sauvegarde_window.title("Champs de saisie")
    InputWindowText = "Fenetre de charger"
    Label(sauvegarde_window, text=InputWindowText).pack()
    sauvegarde_window.geometry("330x120")
    for charge, fichier in charges.items():
        Button(sauvegarde_window, text=charge, command=lambda f=fichier: charger(f)).pack()

def sauvegarder(fichier):
    with open(fichier, 'wb') as f:
        pickle.dump(Sudoku_liste_valeurs, f)

def charger(fichier):
    global Sudoku_liste_valeurs
    with open(fichier, 'rb') as f:
        Sudoku_liste_valeurs = pickle.load(f)
    Sudoku_Update()

sauvegarde_button = Button(root, text="Sauvegarder", command=liste_sauvegarde)
charger_button = Button(root, text="Charger", command=liste_charger)
sauvegarde_button.place(x=605, y=150)
charger_button.place(x=605, y=180)
#-----------------------------------------------------FIN DE JEU------------------------------------------------------
def FinishCheck():
    global Sudoku_liste_valeurs
    for row in range(9):
        for col in range(9):
            if Sudoku_liste_valeurs[row][col] == 0:
                return
    global EndWindow
    EndWindow = Toplevel()
    EndWindow.title("Félicitations!")
    EndText1 = "Vous avez terminé le SUDOKU!!!"
    EndWindow.geometry("490x100")
    Label(EndWindow, text=EndText1).pack()
    EndWindow.mainloop()
    

#--------------------------------------------------FIN DE PROGRAMME---------------------------------------------------
Sudoku_Update()
root.mainloop()
#fin du code