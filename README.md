## TD-02 // Groupe 3 // Sudoku
## https://github.com/uvsq22205472/Sudoku
Ce répertoire était crée pour le module IN200 de l'UFR des Sciences de UVSQ.
Le but est de recréer le jeu de Sudoku avec Python pour ce module.

## Consignes
# Objectif général
Le sudoku est un jeu populaire de placement de nombres basé sur la logique combinatoire. L’objectif est
de remplir une grille 9 × 9 avec des chiffres de sorte que chaque colonne, chaque ligne et chacune des neuf
sous-grilles 3 × 3 qui composent la grille (également appelées "boîtes", "blocs" ou "régions") contiennent
tous les chiffres de 1 à 9.

# Travail demandé
Il faut fournir une interface graphique permettant de jouer au sudoku. Sachant que chaque puzzle doit
avoir une solution unique, l’interface doit pouvoir :
• Générer aléatoirement une grille partiellement remplie respectant la contrainte du sudoku.
• Permettre à l’usager de sélectionner une case et d’entrer un chiffre de 1 à 9 dans cette case.
• Notifier l’utilisateur si le chiffre inséré ne respecte pas les contraintes du jeu.
Votre programme doit également permettre de :
— Proposer une panoplie de puzzles générés auparavant.
— Mettre en évidence les erreurs en utilisant un code couleur (du rouge par exemple) pour montrer la contrainte qui n’est pas respectée.
— Pouvoir annuler une partie de sudoku.
— Effacer des chiffres déjà entrés au niveau des cases.
— Sauvegarder l’état de jeu d’une grille et refaire une grille déjà résolue si l’usager le souhaite.
— Proposer une aide, par exemple afficher toutes les cases contenant un chiffre donné.
— Afficher et sauvegarder le temps nécessaire pour remplir la grille ainsi que le nombre d’erreurs commises.
— Afficher les cases sur lesquelles portent les contraintes (si l’usager le souhaite).

# Pour aller plus loin
Les extensions possibles de ce jeu sont :
— Utiliser une méthode d’IA afin de proposer des aides pertinentes aux joueurs.
— Proposer des niveaux de difficultés différents (suivant le nombre de cases préremplies) en s’assurant
toujours qu’une seule solution existe au puzzle.
— Implémenter une des variantes du sudoku comme le Kakuro, le Kenken, le Hitori ou toute autre
variante.