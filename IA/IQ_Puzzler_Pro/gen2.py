from constante import*
import random


# RAND_GAME_PIECE = random.randint(NB_LINE, NB_LINE*2-1)
RAND_GAME_PIECE = 9


def write_grid(grid):  # écrit la grille dans un fichier
    f = open("grid.txt", "w")

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            f.write(str(grid[l][c]) + " ")
        f.write("\n")

    f.close()

def read_grid(grid):  # lit la grille dans un fichier
    f = open("grid.txt", "r")
    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            grid[l][c] = f.readline().split()

    f.close()

    return grid

def remove_random_pieces(list_piece,list_game_piece,grid):  # enlève des pièces aléatoirement
    for i in range(RAND_GAME_PIECE):
        rand=random.randint(0,len(list_piece)-1)
        list_game_piece.append(list_piece[rand])

        for coordo in list_piece[rand].list:
            (l,c) = coordo
            grid[l][c] = VIDE

        list_piece.remove(list_piece[rand])