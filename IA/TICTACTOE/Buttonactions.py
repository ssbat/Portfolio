from Constante import *
from Affichage import *
def Reset(cnv,grid,player_turn,label:Label):
    cnv.delete("s")
    for i in range(NBCOLUMN):
        for j in range(NBLINE):
            grid[i][j]="_"
    draw_grid(cnv,grid)
    player_turn[0]=0
    label.config(text="Enter Game Mode")
