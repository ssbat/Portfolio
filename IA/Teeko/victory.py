import math

from game_rules import *


def victoire_with_case(ligne, colonne, grid):

    pion = grid[ligne][colonne]
    list_carre = []

    for l in range(ligne-1, ligne+2):
        for c in range(colonne-1, colonne+2):

            if 0 <= l < NB_LINE and 0 <= c < NB_COLUMN:

                if grid[l][c] == pion and (l != ligne or c != colonne):
                    list_carre.append((l, c))
                    count = 2
                    count += search_next_case((ligne, colonne), (l, c), grid, pion)
                    count += search_next_case((l, c), (ligne, colonne),  grid, pion)
                    # print(count)
                    if count >= 4:
                        return True
                    if len(list_carre) == 3:
                        # print("carre :")
                        x, y = width_length_piece(list_carre, ligne, colonne)

                        if norme_vect(x, y) == math.sqrt(8):
                            return True
    return False


def search_next_case(case1, case2, grid, pion):

    (l1, c1) = case1
    (l2, c2) = case2

    l3, c3 = 2 * l2 - l1, 2 * c2 - c1

    if 0 <= l3 < NB_LINE and 0 <= c3 < NB_COLUMN and grid[l3][c3] == pion:

        l4, c4 = 2 * l3 - l2, 2 * c3 - c2

        if 0 <= l4 < NB_LINE and 0 <= c4 < NB_COLUMN and grid[l4][c4] == pion:
            return 2

        return 1

    else:
        return 0


def width_length_piece(list, ligne, colonne):  # retourne la largeur et hauteur

    x = 0
    y = 0
    for i in list:
        (l, c) = i

        x += c - colonne
        y += l - ligne

    return x, y


def norme_vect(x, y):

    return math.sqrt(x**2 + y**2)


def victoire(grid, tour):

    for i in range(0, NB_LINE):
        for z in range(0, NB_COLUMN-3):
            compte = 0
            for j in range(z, z+4):

                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for j in range(0, NB_COLUMN):
        for z in range(0, NB_LINE-3):
            compte = 0
            for i in range(z, z+4):
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for z in range(0, NB_LINE-3):
        for y in range(0, NB_COLUMN-3):
            compte = 0
            for x in range(0, 4):
                l = z + x
                c = y + x
                if grid[l][c] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for y in range(NB_LINE-1, NB_LINE-3, -1):
        for z in range(0, 2):
            compte = 0
            for i in range(y, y-4, -1):
                j = y - i + z
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True