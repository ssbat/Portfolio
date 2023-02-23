from constante import *
from piece import *
from generation import *
import affichage
import itertools
import copy
# list_piece représente la liste des pièces à poser du jeu

def resolve(grid, list_piece, cnv, list_cnv, window):

    liste_piece2=list_piece.copy()
    list_cnv2=list_cnv.copy()

    
    # Initialise affichage gamepieces

    for c in list_cnv:
        c.delete('all')
    list_cnv.clear()

    pos_list = []

    for piece in list_piece:   
        pos_list.append((piece.val, create_possibility_list(grid, piece)))

    # pos_list.append(create_possibility_list(grid, list_piece[0]))

    for row in pos_list:

        val, l_case = row
        # print(len(l_case))
        # print(''.join([str(elem) for elem in row]))

    # print(pos_list)

    affichage.draw_list_pieces(window, list_piece, list_cnv)
    affichage.draw_grid_colour(cnv, grid)

    resolution_1(grid, pos_list, 0)

    affichage.draw_grid_colour(cnv, grid)

    """for p in list_piece:
        print(p.val, ":", p.ref)
        for i in p.list:
            print(i)"""

def generateandtest(grid, list_piece, cnv, list_cnv, window):

    for c in list_cnv:
        c.delete('all')
    list_cnv.clear()

    pos_list = []

    for piece in list_piece:   
        pos_list.append((piece.val, create_possibility_list(grid, piece)))

    # print(pos_list)
    listevaleur=[]
    listepossibleplace=[]
    # print(pos_list)
    for i in pos_list:
        listevaleur.append(str(i[0]))
        # print(i[0])
        listepossibleplace.append(i[1])
    affichage.draw_list_pieces(window, list_piece, list_cnv)
    affichage.draw_grid_colour(cnv, grid)
    combinations = itertools.product(*listepossibleplace)
    result= [
        {
            name: value
            for name, value in zip(listevaleur,combination)
        }
        for combination in combinations
    ]
    print(result)
    i=0
    found=False
    while i<len(result) and found==False:
        #  for possible in result:
        possible=result[i]
        grid2=copy.deepcopy(grid)
        print(grid)
        for val,coord_list in possible.items():
            if not(can_place_w_list(grid2,coord_list)):

                break
            else:
                place_w_list(grid2,coord_list,int(val))
                if is_full(grid2):
                    grid=grid2
                    found=True
                    print("Finally")
                    break
        i=i+1
    affichage.draw_grid_colour(cnv, grid)
    print("Nombre des possibilites:",len(result))




def create_possibility_list(grid, piece):

    possibility_list = []

    #print(piece.redundancy_in_rotation())

    for i in range(piece.redundancy_in_rotation()):

        # piece.is_a_rectangle()
        piece.rotation_piece()
        piece.piece_to_ref()

        for l in range(NB_LINE):
            for c in range(NB_COLUMN):

                case = piece.can_place(grid, (l, c))

                if case:
                    possibility_list.append(case)

    return possibility_list


# pos_list = listes de listes de coordonnées pour chaque pièces

def resolution_1(grid, pos_list, count):

    if is_full(grid):

        print("grille remplie")
        return True
    else:
        # On place les pièces une par une
        val, choice_list = pos_list[count]

        # choice_list = toutes les possibilités de la pièce "count"

        for coord_list in choice_list:

            # coord_list = 1 possibilité de la pièce

            if can_place_w_list(grid, coord_list):#si il y a du place pour la piece
                place_w_list(grid, coord_list, val)#je la place
                count += 1
                if resolution_1(grid, pos_list, count):
                    return True
                else:#si non 
                    count-=1
                    remove_w_list(grid, coord_list)
    return False


def place_w_list(grid, coord_list, val):

    for coord in coord_list:

        (l, c) = coord
        grid[l][c] = val


def can_place_w_list(grid, coord_list):

    for coord in coord_list:

        (l, c) = coord

        if not grid[l][c] == VIDE:
            return False

    return True


def remove_w_list(grid, coord_list):

    for coord in coord_list:

        (l, c) = coord
        grid[l][c] = VIDE