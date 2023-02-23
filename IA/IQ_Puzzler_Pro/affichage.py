import hashlib

from constante import *
from generation import *
from tkinter import *


def draw_grid(cnv):
    # Dessin plateau
    for i in range(0, NB_COLUMN + 1):

        x1 = 4 + i * (COTE_CASE + LINE_WIDTH / 2)
        x2 = x1
        y1 = 0
        y2 = HEIGHT_TAB

        cnv.create_line(x1, y1, x2, y2, width=5, fill='black')

    for j in range(0, NB_LINE + 1):

        y1 = 4 + j * (COTE_CASE + LINE_WIDTH / 2)
        y2 = y1
        x1 = 0
        x2 = WIDTH_TAB

        cnv.create_line(x1, y1, x2, y2, width=5, fill='black')


def draw_grid_colour(cnv, grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            x1 = c * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
            y1 = l * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
            x2 = x1 + COTE_CASE
            y2 = y1 + COTE_CASE

            if grid[l][c] != VIDE:

                color = id_to_random_color(grid[l][c])
                # str(color)
                cnv.create_rectangle(x1, y1, x2, y2, fill='#'+color, width=0)

            else:
                cnv.create_rectangle(x1, y1, x2, y2, fill='white', width=0)


def draw_with_coordo(list_coordo, val, cnv):

    for i in list_coordo:

        (l, c) = i

        x1 = c * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
        y1 = l * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
        x2 = x1 + COTE_CASE
        y2 = y1 + COTE_CASE

        color = id_to_random_color(val)
        # str(color)
        cnv.create_rectangle(x1, y1, x2, y2, fill='#' + color, width=2)


def draw_list_pieces(window, list_piece, list_cnv):

    count = 0

    last_w = 0
    # last_h = 0

    for i in list_piece:

        (h, w) = i.width_length_piece()

        h *= COTE_CASE + LINE_WIDTH
        w *= COTE_CASE + LINE_WIDTH

        cnv = Canvas(window, width=w, height=h, background='light gray')

        cnv.pack()
        cnv.place(x=last_w + count * 20 + TAB_GAP, y=1.5 * TAB_GAP + HEIGHT_TAB)

        draw_with_coordo(i.list, i.val, cnv)

        list_cnv.append(cnv)

        # cnv_game.update()
        last_w += w
        count += 1


def show_number_grid(cnv, grid):

    for i in range(NB_LINE):
        for j in range(NB_COLUMN):

            x = COTE_CASE / 2 + 5 + j * (COTE_CASE + LINE_WIDTH / 2)
            y = COTE_CASE / 2 + 5 + i * (COTE_CASE + LINE_WIDTH / 2)

            if grid[i][j] != 0:
                cnv.create_text(x, y, text=grid[i][j], fill='black', font='Helvetica 30 bold')


def id_to_random_color(number):

    random_bytes = hashlib.sha1(bytes(number)).digest()
    color = [int(random_bytes[-1]), int(random_bytes[-2]), int(random_bytes[-3])]

    for i in range(3):
        if color[i] < 16:
            color[i] += (16 - color[i])
        if color[i] > 255:
            color[i] -= (color[i] - 255)

    result = f'{color[0]:x}' + f'{color[1]:x}' + f'{color[2]:x}'

    return result


