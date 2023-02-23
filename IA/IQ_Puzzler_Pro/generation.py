import affichage
from constante import *
from gen2 import *
import random
from piece import *


def create_grid(grid, list_game_piece, cnv, window, list_cnv):  # fonction dans laquelle nous remplissons la grille

    # Initialisation de la grille avec que des cases vides = 0

    init_grid(grid)

    # count permet de donner une valeur à chaque type de pièces
    count = 1

    # liste contenant toutes les pièces de classe pièce avec valeur, taille et liste de coordonnées
    list_piece = []

    # boucle dans laquelle nos pièces vont être créé, on retourne dans la boucle pour chaques nouvelles pièces
    while not is_full(grid):

        # créer une pièce, la positionne dans la grille et retourne la liste de coordo
        list_coordo = generate_piece(grid, count)

        # ajoute la nouvelle pièce dans liste_piece
        list_piece.append(Piece(count, len(list_coordo), list_coordo))

        count += 1

    # fonction qui permet de fusionner les pièces trop petites
    fusion(list_piece, grid)

    list_game_piece.clear()
    #remove_game_pieces(grid, list_game_piece, list_piece)
    remove_random_pieces(list_piece, list_game_piece, grid)

    # Tourne aléatoirement la pièce puis la place dans ref(0, 0)
    list_piece_to_ref(list_game_piece)

    affichage.draw_grid(cnv)
    affichage.draw_grid_colour(cnv, grid)
    # affichage.show_number_grid(cnv, grid)

    for c in list_cnv:
        c.delete('all')
    list_cnv.clear()

    affichage.draw_list_pieces(window, list_game_piece, list_cnv)

    write_grid(grid)


# Tourne aléatoirement la pièce un certain nombre de fois puis la met dans referentiel (0, 0)

def list_piece_to_ref(list_game_piece):

    for piece in list_game_piece:

        for i in range(random.randint(0, 4)):
            piece.rotation_piece()

        piece.piece_to_ref()


def init_grid(grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            grid[l][c] = VIDE


def fusion(list_piece, grid): # fusionne les pièces de taille 1

    removed_list = []

    for piece in list_piece:

        choice_list = []

        if piece.size == 1:

            removed_list.append(piece)

            (l, c) = piece.list[0]

            for i in range(-1, 2, 2):  # Parcours les cases adjacentes

                if 0 <= l + i < NB_LINE:

                    for p2 in list_piece:

                        if grid[l + i][c] == p2.val:

                            choice_list.append(p2)

                if 0 <= c + i < NB_COLUMN:

                    for p2 in list_piece:

                        if grid[l][c + i] == p2.val:

                            choice_list.append(p2)

            s_max = 10
            choosed_piece = None

            for ch in choice_list:   # choisit la pièce avec le moins de case

                p2 = ch

                if p2.size < s_max:
                    s_max = p2.size
                    choosed_piece = p2

            grid[l][c] = choosed_piece.val
            # list_piece.remove(piece)

            choosed_piece.size += 1
            choosed_piece.list.append((l, c))

    for not_piece in removed_list:
        list_piece.remove(not_piece)


def is_full(grid): # vérifier que la grille ne contient aucun 0

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] == VIDE:
                return False
    return True


def generate_piece(grid, count): #genere une pièce dans la grille

    choice_list = [] #cases qui peuvent être élues
    choosed_list = [] # cases qui composent la pièce

    l = random.randint(0, NB_LINE - 1)
    c = random.randint(0, NB_COLUMN - 1)

    while grid[l][c] != VIDE:
        l = random.randint(0, NB_LINE - 1)
        c = random.randint(0, NB_COLUMN - 1)

    N = size_piece()

    grid[l][c] = count
    choosed_list.append((l, c))  # ajoute la case à la liste des cases de la pièce

    N -= 1

    while N > 0:

        for i in range(-1, 2, 2):

            if 0 <= l + i < NB_LINE and grid[l + i][c] == VIDE:

                if choice_list.count((l + i, c)) == VIDE:  # vérifie qu'on peut s'étendre

                    # ajoute la case à la liste des cases qui peuvent être élues
                    choice_list.append((l + i, c))

            if 0 <= c + i < NB_COLUMN and grid[l][c + i] == VIDE:

                if choice_list.count((l, c + i)) == 0:
                    choice_list.append((l, c + i))

        if len(choice_list) < 1:
            break

        rand = random.randint(0, len(choice_list) - 1)

        (l2, c2) = choice_list[rand]

        choice_list.remove((l2, c2))

        grid[l2][c2] = count

        choosed_list.append((l2, c2))

        (l, c) = (l2, c2)

        N -= 1

    return choosed_list


def size_piece():  # renvoie la taille de la pièce en fonction de probabilités
    r = random.randint(1, 10)

    if r <= 4:
        N = 5

    elif r <= 7:
        N = 4

    elif random.randint(1, 2) == 1:
        N = 3

    else:
        N = 6

    return N


# fonction qui enlève les pièces se trouvant en bas du plateau

def remove_game_pieces(grid, list_game_piece, list_piece):

    for c in range(NB_COLUMN):
        val = grid[NB_LINE - 1][c]

        if val != VIDE:

            for p in list_piece:

                if p.val == val:
                    list_game_piece.append(p)
                    list_piece.remove(p)

                    for c_p in p.list:
                        (l, c) = c_p
                        grid[l][c] = VIDE






