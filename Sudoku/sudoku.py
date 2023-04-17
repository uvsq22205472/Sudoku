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

global Canvas_Longeur
global Canvas_Largeur

global Sudoku_ListeValeurs
Sudoku_ListeValeurs = [[0 for i in range(9)] for j in range(9)]
global Sudoku_ValeursImpermeables
Sudoku_ValeursImpermeables = [[0 for i in range(9)] for j in range(9)]

global siJeuCommence
siJeuCommence = False
Canvas_Largeur = 600
Canvas_Longeur = 600

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Initialisation du tableau du jeu-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

root = Tk()
root.title("Sudoku")
root.geometry("750x600")
# --> https://www.tutorialspoint.com/how-can-i-prevent-a-window-from-being-resized-with-tkinter
root.resizable(False,False)

Sudoku_Canvas = Canvas(root,bg='#CCCCCC', width= Canvas_Largeur, height= Canvas_Longeur)
Sudoku_Canvas.grid(column=0,row=0,columnspan=20,rowspan=20)


#----------------------------------------------Entrer valeur---------------------------------------------------------

global Erreurs
Erreurs = 0

def Nombre_Erreurs():
    """
    Output: Erreurs ()
    Fonction qui renvoie les erreurs.
    """
    global Erreurs
    return Erreurs


Ecriture_Nombre_Erreurs = Label(font=('Arial Black', 18), text=f"Erreurs: {Nombre_Erreurs()}")
Ecriture_Nombre_Erreurs.place(x=610, y=300)

def Fenetre_Entree_Valeur(event):
    """
     Cette fonction permet de rentré dans la fenetre des valeur et les entré dans le tableaux 
    """
    #Position du clic
    x, y = event.x, event.y
    #Calculer la position de la case par rapport au clic
    col = int(x // (Canvas_Largeur / 9))
    row = int(y // (Canvas_Longeur / 9))
    print("ROW / COL :",row,col)
    print("LIST :",Sudoku_ListeValeurs)
    print("Rigid Cells:",Sudoku_ValeursImpermeables)
    if (Sudoku_ValeursImpermeables[row][col] == -1) or (siJeuCommence == False):
        return None
    #Fenetre
    Fenetre_Entree = Toplevel(root)
    Fenetre_Entree.title("Champs de saisie")
    # --> https://datatofish.com/Entree-box-tkinter/
    # --> https://stackoverflow.com/questions/42211865/how-to-add-text-to-a-toplevel-window
    Fenetre_Entree_Texte = "\nVeuillez entrer une valeur comprise entre 1 et 9 puis Valider\nou cliquer sur Effacer pour effacer la valeur dans la case."
    Label(Fenetre_Entree, text=Fenetre_Entree_Texte, bg='grey90',height=3).pack()
    # -- -- --
    Fenetre_Entree.geometry("330x160")

    #Champs de saisie
    Entree = Entry(Fenetre_Entree)
    Entree.pack(pady=10)

    #Placer dans la case du sudoku
    def Placer_Valeur():
        """
        Cette fonction permet de placer la valeur sélectionnée dans la cellule sélectionnée et vérifie si cette 
        valeur respecte les régles et modifie le texte en conséquence.Si aucune valeur n'est entrée alors la valeur 
        devient 0 et donc efface la casse 
        """
        global Erreurs
        CelluleSelectionee = "Cellule"+str(row)+";"+str(col)
        Valeur = Entree.get() 
        if Valeur.isnumeric() == True and 1<=int(Valeur)<=9:
            Valeur = int(Valeur)
            if Verification_Contraintes(row,col, Valeur) == True:
                #pour placer le Cellule_Text + au milieux de la case (1/18)
                Sudoku_ListeValeurs[row][col] = Valeur
                x1 = (col/9)*Canvas_Largeur + (Canvas_Largeur/18)
                y1 = (row/9)*Canvas_Longeur + (Canvas_Longeur/18)
                Cellule = Sudoku_Canvas.find_withtag(CURRENT)
                Cellule_Text = Sudoku_Canvas.delete(CelluleSelectionee)
                Cellule_Text = Sudoku_Canvas.create_text(x1, y1, text=Valeur, font=("Helvetica", 16),tag=CelluleSelectionee)
                Sudoku_Canvas.itemconfig(Cellule, text=Cellule_Text)
                print(Sudoku_ListeValeurs)
            else:
                Erreurs = Erreurs + 1
                messagebox.showerror(title="Erreur",message="Verifiez que votre valeur n'est pas déjà présente sur la ligne, la colonne ou encore la région.")
        elif Valeur == "":
            erase_value()
            #Si rien est entre dans, alors cela suprime la valeur dans la case et met 0 dans le tableau.
        else:
            Erreurs = Erreurs + 1
            messagebox.showerror(title="Erreur",message="Veillez à entrer un chiffre compris entre 1 et 9.")
        Fenetre_Entree.destroy()
        Sudoku_Update()
        Ecriture_Nombre_Erreurs.config(text=f"Erreurs: {Nombre_Erreurs()}")
    def erase_value():
        """
        imput: erase_value (str) = effacer les valeur précédant 
        output : nope ceci signifie que les casse sont vide 
        Cette fonction d'enlever des valeurs de certaine casse 
        """
        CelluleSelectionee = "Cellule"+str(row)+";"+str(col)
        Sudoku_ListeValeurs[row][col]= 0
        Cellule_Text = Sudoku_Canvas.delete(CelluleSelectionee)
        Fenetre_Entree.destroy()
        Sudoku_Update()
        return None
    #creation d'un bouton pour valider la saisie et placer la valeur dans la case du sudoku
    button = Button(Fenetre_Entree, text="Valider", command=Placer_Valeur, bg='SeaGreen1')
    button.pack()

    erase_button = Button(Fenetre_Entree,text="Effacer", command=erase_value, bg='coral1')
    erase_button.pack()
def Verification_Contraintes(row, col, num):
    """
    imput : row,col,num (int) = vérificatiob si la case valide les contraite du jeux 
    output : false si les contrainte sont pas réspectés
            trua si elle le sont 
    Cette fonction permet de vérifier qu'il n'y a pas le meme nombres sur les meme ligne et colonne et que la 
    configuration des nombres soit bien respectée 
    """
    # Verif pour les lignes
    if num in Sudoku_ListeValeurs[row]:
        return False
    # Verif pour les colonnes
    for i in range(len(Sudoku_ListeValeurs)):
        if Sudoku_ListeValeurs[i][col] == num:
            return False
    # Verif pour le carree
    SquareRow = (row // 3) * 3
    SquareCol = (col // 3) * 3
    for i in range(SquareRow, SquareCol + 3):
        for j in range(SquareRow, SquareCol + 3):
            if Sudoku_ListeValeurs[i][j] == Sudoku_ListeValeurs:
                return False

    return True

#----------------------------------------------Géneration aléatoire de tableau ---------------------------------------------------------
# Generation du tableau completement aleatoire
def Sudoku_GenererTableau(difficulte: str):
    """Input : difficulte (str) = Difficulté choisie par l'utiliseur
    Output : Sudoku_ListeValeurs (list) = Tableau de Sudoku utilisé par le jeu

    Cette fonction génére un tableau de jeu de Sudoku complete avant de le vider selon la difficulté choisi.
    La difficulté influence le nombre des cases à vider, puis cette fonction renvoie le tableau et met à jour le tableau pour
    l'afficher.
    
    """
    global Sudoku_ListeValeurs
    Sudoku_FillBoard(Sudoku_ListeValeurs)
    Sudoku_UnfillBoard(Sudoku_ListeValeurs, difficulte)
    print(Sudoku_ListeValeurs)
    Sudoku_Update()
    return Sudoku_ListeValeurs

def Sudoku_FillBoard(board: list):
    """
    Input: board (list) = 
    Output: True = si le tableau est rempli
            False = si le tableau ne peut pas etre rempli
    Cette fonction permet de remplir chaque case du tableau lorsqu'elles sont vides.

    """
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
    """
    imput : bord (list) = vérification des casse vide 
    output : (i,j) si y'a un 0 dans le tableaux 
             none si il n'y a pas de 0 
    Cette fonction permet de vérifier que chaque case du tableaux lorsqu'elle sont vide j'usqua la dernière  de la grille c'est à dire 
    la 9 émé 
    """
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def ValidCellCheck(board: list, row: int, col: int, val: int):
    """
    Input: board (list): le tableau à vérifier
            row (int): ligne
            col (int): colonne
            val (int): valeur à vérifier

    Cette fonction vérifie si la valeur généré est déja présente dans la colonne , ligne et carré.

    """
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

def Sudoku_UnfillBoard(board: list, difficulte: str):
    """
    imput: board (list),dificulty(str) = remplir le tableaux en fonction du nive    aux de difficukté 
    output: False = la difficulté n'est oas disponible 
    True = quand le processuse de déremplissage est validé en fonction de la difficulté choisi 
    Cette fonction permet d'effacer chaque case du tableaux lorsqu'elle sont remplis en fonction de la difficulté
    c'est a dire  le nombres de case remplis sera en fonction du niveaux de difficulté (esay,normal,hard)

    """
    if difficulte == 'easy':
        CellsToRemove = randint(35, 45)
    elif difficulte == 'medium':
        CellsToRemove = randint(46, 55)
    elif difficulte == 'hard':
        CellsToRemove = randint(56, 65)
    else:
        print("Erreur: la difficulté n'est pas disponible")
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
    """
    Input: Sudoku_ListeValeurs (list) : le tableau qui va être mis à jour
    Output: Sudoku_ListeValeurs (list) : le tableau mis à jour

    Cette fonction traverse le tableau et re-écrit dans chaque case le nombre correspondant. Cela sert à réinitialiser le tableau et mettre à jour les valeurs si il y
    a une mauvaise correspendance entre le tableau du jeu et le tableau visuel.
    Les 0 sont traduits comme des cases vides et sont donc montrés comme tels.

    """
    global Sudoku_ListeValeurs
    #print("ENTRY",Sudoku_ListeValeurs)
    row , col = 0, 0
    for row in range(9):
        for col in range(9):
            CelluleSelectionee = "Cellule"+str(row)+";"+str(col)
            x1 , y1 = (col/9)*Canvas_Largeur + (Canvas_Largeur/18) , (row/9)*Canvas_Longeur + (Canvas_Longeur/18)
            Cellule = Sudoku_Canvas.find_withtag(CURRENT)
            Cellule_Text = Sudoku_Canvas.delete(CelluleSelectionee)
            if Sudoku_ListeValeurs[row][col] != 0:
                Cellule_Text = Sudoku_Canvas.create_text(x1, y1, text=Sudoku_ListeValeurs[row][col], font=("Helvetica", 16),tag=CelluleSelectionee)
            else:
                Cellule_Text = Sudoku_Canvas.create_text(x1, y1, text="", font=("Helvetica", 16),tag=CelluleSelectionee)
            Sudoku_Canvas.itemconfig(Cellule, text=Cellule_Text)
    #print("LAST",Sudoku_ListeValeurs)
    Verification_FinJeu()
    return Sudoku_ListeValeurs
     
def Initialisation_Jeu(difficulte: str):
    """
    Input: difficulte (str): niveau de difficulté selectionné par l'utilisateur.
    Output: Sudoku_ListeValeurs (list): tableau du jeu

    Cette fonction initialise / réinitialise le tableau du jeu selon la difficulté avec son tableau de nombres impérméables correspondant et
    met en marche la détection d'erruers ainsi que le Timer.

    """
    global Sudoku_ListeValeurs
    global Sudoku_ValeursImpermeables
    global Minutes , Secondes
    global siJeuCommence
    global Erreurs

    Erreurs = 0
    Ecriture_Nombre_Erreurs.config(text=f"Erreurs: {Nombre_Erreurs()}")

    if difficulte == "easy" or difficulte == "medium" or difficulte == "hard":
        Sudoku_ListeValeurs = [[0 for i in range(9)] for j in range(9)]
        Sudoku_ListeValeurs = Sudoku_GenererTableau(difficulte)
        Sudoku_ValeursImpermeables =  [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if Sudoku_ListeValeurs[i][j] == 0:
                    Sudoku_ValeursImpermeables[i][j] = 0 
                else:
                    Sudoku_ValeursImpermeables[i][j] = -1
    else:
        Grilles_Generes_Auparavant(difficulte)
# Mettre redemarrer Timer
    if not Timer_en_Marche:
        Demarrer_Timer()
    else:
        Redemarre_Timer()
    Sudoku_Update()
    Fenetre_Difficulte.destroy()
    siJeuCommence = True
    return Sudoku_ListeValeurs


def Fenetre_Debuter():
    """
    Input: xxx
    Output: xxx

    Crée un tableau qui sert de sélectionner la difficulté ainsi que le mode (Aléatoire // Pré-généré)
    """
    global Fenetre_Difficulte
    Fenetre_Difficulte = Toplevel()
    Fenetre_Difficulte.title("Choix de la difficulté")
    Texte_Difficulte = "Choisissez une grille aléatoire ou pré-généré"
    Fenetre_Difficulte.geometry("490x100")
    Label(Fenetre_Difficulte, text=Texte_Difficulte).grid(column=1)
    Bouton_Facile = Button(Fenetre_Difficulte,fg='green' ,text="Aléatoire : Facile", command=lambda: Initialisation_Jeu("easy"))
    Bouton_Facile.grid(column=0,row=4,padx=15)

    Bouton_Moyen = Button(Fenetre_Difficulte,fg='orange', text="Aléatoire : Moyen", command=lambda: Initialisation_Jeu("medium"))
    Bouton_Moyen.grid(column=0,row=6)

    Bouton_Difficile = Button(Fenetre_Difficulte,fg='red' ,text="Aléatoire : Difficile", command=lambda: Initialisation_Jeu("hard"))
    Bouton_Difficile.grid(column=0,row=8)

    Bouton_Facile_PreRempli = Button(Fenetre_Difficulte, fg='green',text="Pré-généré : Facile", command=lambda: Initialisation_Jeu("facile"))
    Bouton_Facile_PreRempli.grid(column=4,row=4)

    Bouton_Moyen_PreRempli = Button(Fenetre_Difficulte,fg='orange' ,text="Pré-généré : Moyen", command=lambda: Initialisation_Jeu("moyen"))
    Bouton_Moyen_PreRempli.grid(column=4,row=6)

    Bouton_Difficle_PreRempli = Button(Fenetre_Difficulte,fg='red' ,text="Pré-généré : Difficile", command=lambda: Initialisation_Jeu("difficile"))
    Bouton_Difficle_PreRempli.grid(column=4,row=8)
    Fenetre_Difficulte.mainloop()

def Grilles_Generes_Auparavant (difficulte: str):
    """
    Input: difficulte (str): difficulté, ici soit "facile" "moyen" ou "difficile" uniquement ( les noms en anglais sont réservés pour les tableaux générés
                             aléatoirement)
    Output: Sudoku_ListeValeurs (list): tableau du jeu

    Cette fonction remplace le tableau par un tableau prédéfini selon la difficulté. Si aucun n'est écrit alors une erreur apparaît.
    """
    global Sudoku_ListeValeurs

    if difficulte == "facile":
        Sudoku_ListeValeurs = [
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
        print(Sudoku_ListeValeurs)
    elif difficulte == "moyen":
        Sudoku_ListeValeurs = [
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
        print(Sudoku_ListeValeurs)
    elif difficulte == "difficile":
        Sudoku_ListeValeurs = [
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
        print(Sudoku_ListeValeurs)
    else:
        print("Difficulté non valide")
        return None
    return Sudoku_ListeValeurs


#----------------------------------------------Timer-----------------------------------------------------------------

Timer_en_Marche = False
Minutes = 0
Secondes = 0
'''Chronometre avec 3 fonctions demarrer, eteindre et redemarrer'''

def Demarrer_Timer():
    """
    Fonction qui demarre le timer si il n'est pas allumé déjà.
    """
    global Timer_en_Marche
    if not Timer_en_Marche:
        Timer_en_Marche = True
        Timer()

def Arreter_Timer():
    """
    Fonction qui arrête le timer si il est allumé et le remet à 0.
    """
    global Timer_en_Marche
    if Timer_en_Marche:
        Timer_en_Marche = False
        Ecriture_Timer.after_cancel(MAJ_Timer)
        Minutes = 0
        Secondes = 0
        Timer()

def Redemarre_Timer():
    """
    Fonction qui rédemarre le timer sur la base des deux fonction précedentes.
    """
    global Timer_en_Marche
    if Timer_en_Marche:
        Arreter_Timer()
        Demarrer_Timer()

def Timer():
    """
    Fonction qui sert de minuteur et donne son écritures en minutes et secondes.
    """
    if Timer_en_Marche == True:
        global Minutes, Secondes
        Secondes = Secondes + 1
        Ecriture_Minutes = f'{Minutes}' if Minutes > 9 else f'0{Minutes}'
        Ecriture_Secondes = f'{Secondes}' if Secondes > 9 else f'0{Secondes}'
        Ecriture_Timer.config(text=Ecriture_Minutes + ':' + Ecriture_Secondes)
        if Secondes == 60:
            Minutes = Minutes + 1
            Secondes = 0
        global MAJ_Timer
        MAJ_Timer = Ecriture_Timer.after(1000, Timer)
    else:
        Minutes = 0
        Secondes = 0

Ecriture_Timer = Label(font=('Helvetica', 30), text='00:00')
Ecriture_Timer.place(x=620, y=10)

Bouton_Start = Button(text='Débuter', height=1, width=8, font=('Helvetica', 22), command=Fenetre_Debuter)
Bouton_Start.place(x=605, y=80)
#----------------------------------------------Dessin Graphique---------------------------------------------------------


#boucle for pour dessiner les rectangles
for i in range(0, 9):
    for j in range(0, 9):
        x1, y1 = (j/9)*Canvas_Largeur, (i/9)*Canvas_Longeur
        x2, y2 = ((j+1)/9)*Canvas_Largeur, ((i+1)/9)*Canvas_Longeur
        Rectangle = Sudoku_Canvas.create_rectangle(x1, y1, x2, y2, width=1, outline='gray',fill="gray90")
        Sudoku_Canvas.tag_bind(Rectangle, '<Button-1>', Fenetre_Entree_Valeur)
        Sudoku_Canvas.grid(row=i, column=j)
#boucle for pour dessiner les regions
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        x1, y1 = (j/9)*Canvas_Largeur, (i/9)*Canvas_Longeur
        x2, y2 = ((j+3)/9)*Canvas_Largeur, ((i+3)/9)*Canvas_Longeur
        Sudoku_Canvas.create_rectangle(x1, y1, x2, y2, width=3)
        Sudoku_Canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, width=4, outline="white")

#------------------------------------------------MENU-------------------------------------------------------------

#Barre de menu
Barre_Menus = Menu(root)
Menu_Grille = Menu(Barre_Menus, tearoff=0)

def Ouvrir_Lien_Regles():
    webbrowser.open('https://sudoku.com/fr/comment-jouer/regles-de-sudoku-pour-les-debutants-complets/')

Menu_Aide = Menu(Barre_Menus, tearoff=0)
Barre_Menus.add_cascade(label="Aide", menu=Menu_Aide)
Menu_Aide.add_command(label="Règle du Sudoku",command=Ouvrir_Lien_Regles)

root.config(menu=Barre_Menus)
#------------------------------------------------------Annuler------------------------------------------------------------
"""Fonction pour quitter, efface tout"""
def Annuler_Partie():
    """
    Input: xxx
    Output: Sudoku_ListeValeurs (list) : tableau du jeu annulé et remis à 0.
            Sudoku_ValeursImpermeables (list) : tableau des cases imperméables du jeu remis à 0.
    Cette fonction annule la partie en remettant à 0 les deux listes et le timer ainsi que les 0.
    """
    global Sudoku_ListeValeurs
    global Sudoku_ValeursImpermeables
    global siJeuCommence
    global Erreurs

    Sudoku_ValeursImpermeables = [[0 for i in range(9)] for j in range(9)]
    Sudoku_ListeValeurs = [[0 for i in range(9)] for j in range(9)]
    Arreter_Timer()
    Sudoku_Update()
    Erreurs = 0
    Ecriture_Nombre_Erreurs.config(text=f"Erreurs: {Nombre_Erreurs()}")
    print(Sudoku_ListeValeurs)
    siJeuCommence = False
    return Sudoku_ListeValeurs, Sudoku_ValeursImpermeables

Bouton_Annuler = Button(root, text="Annuler la partie", command=Annuler_Partie, bg='grey70', relief=RIDGE)
Bouton_Annuler.place(x=605, y=220)

#------------------------------------------------------Sauvegarde------------------------------------------------------------
#https://www.quennec.fr/trucs-astuces/langages/python/python-le-module-pickle
#On a mis en dictionnaire pour pas refaire 3x la meme fonction

Sauvegardes = {
    'sauvegarde 1': 'sudoku.grille',
    'sauvegarde 2': 'sudoku.grille2',
    'sauvegarde 3': 'sudoku.grille3'
}

Charges = {
    'charge 1': 'sudoku.grille',
    'charge 2': 'sudoku.grille2',
    'charge 3': 'sudoku.grille3'
}

def Liste_Sauvegardes():
    """
    Fonction occupé de la fenêtre des sauvegardes.
    """
    Fenetre_Sauvegardes = Toplevel(root)
    Fenetre_Sauvegardes.title("Champs de saisie")
    Fenetre_Entree_Texte = "Fenêtre de Sauvegarde"
    Label(Fenetre_Sauvegardes, text=Fenetre_Entree_Texte).pack()
    Fenetre_Sauvegardes.geometry("330x120")
    for sauvegarde, fichier in Sauvegardes.items():
        Button(Fenetre_Sauvegardes, text=sauvegarde, command=lambda f=fichier: Sauvegarder(f)).pack()

def Liste_Charges():
    """
    Fonction occupé de la fenêtre des charges.
    """
    Fenetre_Charges = Toplevel(root)
    Fenetre_Charges.title("Champs de saisie")
    Fenetre_Entree_Texte = "Fenêtre des parties Charger"
    Label(Fenetre_Charges, text=Fenetre_Entree_Texte).pack()
    Fenetre_Charges.geometry("330x120")
    for charge, fichier in Charges.items():
        Button(Fenetre_Charges, text=charge, command=lambda f=fichier: Charger(f)).pack()

def Sauvegarder(fichier):
    """
    Input: fichier (str) : le nom du fichier dans lequel va se trouver la sauvegarde.
    Cette fonction remet la liste Sudoku_ListeValeurs dans le fichier.
    """
    with open(fichier, 'wb') as f:
        pickle.dump(Sudoku_ListeValeurs, f)


def Charger(fichier):
    """
    Input: fichier (str) : nom du fichier à chercher
    Cette fonction récupère la liste Sudoku_ListeValeurs dans le fichier.
    """
    global Sudoku_ListeValeurs
    global Erreurs
    with open(fichier, 'rb') as f:
        Sudoku_ListeValeurs = pickle.load(f)
    Sudoku_Update()
    Erreurs = 0
    Ecriture_Nombre_Erreurs.config(text=f"Erreurs: {Nombre_Erreurs()}")

Bouton_Sauvegarder = Button(root, text="Sauvegarder", command=Liste_Sauvegardes, bg='grey70', relief=RIDGE)
Bouton_Charger = Button(root, text="Charger", command=Liste_Charges, bg='grey70', relief=RIDGE)
Bouton_Sauvegarder.place(x=605, y=150)
Bouton_Charger.place(x=605, y=180)
#-----------------------------------------------------FIN DE JEU------------------------------------------------------
def Verification_FinJeu():
    """
    Cette fonction vérifie si toute les cases sont remplies et affiche le temps et le nombres d'erreurs commises.
    """
    global Sudoku_ListeValeurs
    for row in range(9):
        for col in range(9):
            if Sudoku_ListeValeurs[row][col] == 0:
                return
    global Fenetre_FinJeu
    Fenetre_FinJeu = Toplevel()
    Fenetre_FinJeu.title("Fin de la partie !")
    Fenetre_FinJeu.geometry("540x65")

    Texte_FinJeu1 = f"Félicitations! Vous avez fini la partie de Sudoku en : {int(Minutes)} Minutes et {int(Secondes):02d} Secondes !\n Vous avez fait au totale : {int(Erreurs)} Erreurs"
    Label_FinJeu = Label(Fenetre_FinJeu, text=Texte_FinJeu1, font=("Helvetica", 11), pady=10, bg='grey90')    
    Label_FinJeu.pack()

    Arreter_Timer()
    Fenetre_FinJeu.mainloop()
    

#--------------------------------------------------FIN DE PROGRAMME---------------------------------------------------
Sudoku_Update()
root.mainloop()
#fin du code