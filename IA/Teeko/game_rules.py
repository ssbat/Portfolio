from constante import *
import affichage
import victory
import intelligence as ia
import time


def clickcase(event, grid, tour, list_pos, all_canvas, typeGame):

    if typeGame[0] != NO_GAME:

        cnv, cnv1, cnv2, cnv_text = all_canvas

        # Première partie du jeu où il faut positionner les pièces

        if tour[0] < 8:
            ligne = int(event.y / (HEIGHT_TAB/NB_LINE))
            colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

            if grid[ligne][colonne] == '_':
                pion = pion_tour(tour[0])
                grid[ligne][colonne] = pion
                affichage.draw_piece(cnv, ligne, colonne, pion)

                if pion == 'x':
                    cnv1.config(width=(3-int(tour[0]/2))*(COTE_CASE+LINE_WIDTH))
                else:
                    cnv2.config(width=(3-int(tour[0]/2))*(COTE_CASE+LINE_WIDTH))

                if victory.victoire_with_case(ligne, colonne, grid):
                    print(f'Victoire, {pion_tour(tour[0])} ')
                    affichage.disp_win(tour[0], cnv_text)
                else:
                    tour[0] += 1

                    if typeGame[0] == ORDI:

                        tps1 = time.time()

                        l, c = ia.choix_case(grid, tour[0], cnv)

                        tps2 = time.time()
                        print("time = ", tps2 - tps1)

                        if pion == 'x':
                            cnv2.config(width=(3 - int(tour[0] / 2)) * (COTE_CASE + LINE_WIDTH))
                        else:
                            cnv1.config(width=(3 - int(tour[0] / 2)) * (COTE_CASE + LINE_WIDTH))

                        if victory.victoire_with_case(l, c, grid):
                            print(f'Victoire, {pion_tour(tour[0])} ')
                            affichage.disp_win(tour[0], cnv_text)
                        else:
                            tour[0] += 1
                            cnv.update()



        # Deuxième partie
        # Click sur la case qu'on veut déplacer

        elif not list_pos:

            ligne = int(event.y / (HEIGHT_TAB / NB_LINE))
            colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

            if grid[ligne][colonne] == pion_tour(tour[0]):

                list_pos.append((ligne, colonne))
                list_pos.append(possibility_case(ligne, colonne, grid, cnv))

        # Choix du coup à effectuer par rapport à la pièce sélectionner

        else:
            # print("second")
            # print(list_pos)

            ligne = int(event.y / (HEIGHT_TAB / NB_LINE))
            colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

            last_case = list_pos[0]
            list_case = list_pos[1]

            # Coup valide

            if (ligne, colonne) in list_case:

                move_the_piece(ligne, colonne, list_case, last_case, grid, tour, cnv)
                if victory.victoire_with_case(ligne, colonne, grid):
                    print(f'Victoire, {pion_tour(tour[0])} ')
                    affichage.disp_win(tour[0], cnv_text)
                else:
                    tour[0] += 1

                    # Coup de l'ordinateur

                    if typeGame[0] == ORDI:

                        tps1 = time.time()

                        l, c = ia.choix_case(grid, tour[0], cnv)

                        tps2 = time.time()
                        print("time = ", tps2 - tps1)

                        if victory.victoire_with_case(l, c, grid):
                            print(f'Victoire, {pion_tour(tour[0])} ')
                            affichage.disp_win(tour[0], cnv_text)
                        else:
                            tour[0] += 1
                            cnv.update()

                list_pos.clear()

            # Changement de pièce sélectionner

            elif grid[ligne][colonne] == pion_tour(tour[0]):

                hide_case(list_case, cnv)
                list_pos.clear()
                list_pos.append((ligne, colonne))
                list_pos.append(possibility_case(ligne, colonne, grid, cnv))
                cnv.update()

            # Coup non valide, déselectionne la pièce

            else:
                hide_case(list_case, cnv)
                list_pos.clear()


def move_the_piece(ligne, colonne, list_case, last_case, grid, tour, cnv):

    last_l, last_c = last_case

    list_case.remove((ligne, colonne))
    # print("good_line")

    pion = pion_tour(tour[0])

    affichage.remove_piece(cnv, last_l, last_c)
    grid[last_l][last_c] = '_'

    affichage.draw_piece(cnv, ligne, colonne, pion)
    grid[ligne][colonne] = pion

    hide_case(list_case, cnv)


def possibility_case(l, c, grid, cnv):

    list_pos = []
    for i in range(l-1, l+2):
        for j in range(c-1, c+2):

            if 0 <= i < NB_LINE and 0 <= j < NB_COLUMN and grid[i][j] == '_':
                affichage.draw_possible_case(cnv, i, j, "red")
                list_pos.append((i, j))
    return list_pos


def hide_case(list_pos, cnv):

    for i in list_pos:

        l, c = i

        affichage.hide_possible_case(cnv, l, c)


def pion_tour(tour):

    if tour % 2 == 0:
        return 'x'
    else:
        return 'o'



