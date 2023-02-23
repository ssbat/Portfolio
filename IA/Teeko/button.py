from constante import *
from affichage import *
import intelligence as ia


def toggle_ami(button_ami, button_ordi, typeGame, cnv_text):

    if button_ami.config('relief')[-1] == 'sunken':
        button_ami.config(relief="raised")
    else:
        button_ami.config(relief="sunken")
        typeGame[0] = AMI
        if button_ordi.config('relief')[-1] == 'sunken':
            button_ordi.config(relief="raised")

    cnv_text.delete('all')
    cnv_text.create_text(COTE_CASE * 2, COTE_CASE / 2, text="Let's play !", fill="black",
                         font='Helvetica 18 bold')


def toggle_ordi(button_ami, button_ordi, typeGame, cnv_text):

    if button_ordi.config('relief')[-1] == 'sunken':
        button_ordi.config(relief="raised")
    else:
        button_ordi.config(relief="sunken")
        typeGame[0] = ORDI

        if button_ami.config('relief')[-1] == 'sunken':
            button_ami.config(relief="raised")
    cnv_text.delete('all')
    cnv_text.create_text(COTE_CASE * 2, COTE_CASE / 2, text="Let's play !", fill="black",
                         font='Helvetica 18 bold')


def reset_grid(grid, tour, typeGame, button_ami, button_ordi, all_canvas):

    cnv, cnv1, cnv2, cnv_text = all_canvas

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            grid[l][c] = '_'

    tour[0] = 0
    print("okk")
    draw_grid(cnv)
    draw_list_pieces(cnv1, cnv2)
    cnv1.config(width=4*(COTE_CASE+LINE_WIDTH))
    cnv2.config(width=4 * (COTE_CASE + LINE_WIDTH))
    # cnv.update()

    if button_ordi.config('relief')[-1] == 'sunken':
        typeGame[0] = ORDI
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Let's play !", fill="black",
                             font='Helvetica 18 bold')

    elif button_ami.config('relief')[-1] == 'sunken':
        typeGame[0] = AMI
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 2, COTE_CASE / 2, text="Let's play !", fill="black",
                             font='Helvetica 18 bold')


def ordi_vs_ordi(grid, tour, cnv):

    l, c = None, None
    not_finished = True

    while not_finished:

        l, c = ia.choix_case(grid, tour[0], cnv)

        if victory.victoire_with_case(l, c, grid):
            print(f'Victoire, {pion_tour(tour[0])} ')
            not_finished = False
            # affichage.disp_win(tour[0], cnv_text)
        else:
            tour[0] += 1
            cnv.update()

