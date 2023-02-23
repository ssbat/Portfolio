
from affichage import *
from generation import *
from piece import *
from resolution import *

window = Tk()
window.title("IQ Puzzler Pro")
window.geometry("1080x720")

cnv_game = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

cnv_game.pack()
cnv_game.place(x=TAB_GAP, y=TAB_GAP)

# cnv_piece = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

# cnv_piece.pack()
# cnv_piece.place(x=TAB_GAP, y=1 * TAB_GAP + HEIGHT_TAB)

draw_grid(cnv_game)

grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]
list_game_piece = []
list_cnv = []

generate_button = Button(window, text="Générer", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: create_grid(grid, list_game_piece, cnv_game, window, list_cnv)))

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=2 * TAB_GAP)

verify_button = Button(window, text="Verifier avec T&G", font='Helvetica 15 bold',
                         background='light gray', command=(lambda: resolve(grid, list_game_piece, cnv_game, list_cnv, window)))

verify_button.place(x=2 * TAB_GAP + WIDTH_TAB, y= 3 * TAB_GAP)

# verify_buttonGenAndTest = Button(window, text="Verifier avec G&T", font='Helvetica 15 bold',
#                          background='light gray', command=(lambda: generateandtest(grid, list_game_piece, cnv_game, list_cnv, window)))

# verify_buttonGenAndTest.place(x=2 * TAB_GAP + WIDTH_TAB, y= 4 * TAB_GAP)

window.mainloop() 
#hon tab3 mini size ha ykun (0,0) laan l-l =0 et c-c=0