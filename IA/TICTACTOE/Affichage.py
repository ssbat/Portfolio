from Constante import *
from tkinter import*

def create_cnv(cnv):
    for nc in range(1,NBCOLUMN):
        cnv.create_line(0+GAP*nc,0,0+GAP*nc,HEIGHT,fill='red',width=5)

    for nl in range(1,NBLINE):
        cnv.create_line(0,0+GAP*nl,600,0+GAP*nl,fill='red',width=5)

def draw_grid(cnv:Canvas,grid):
    for lineIndex,line in enumerate(grid):
        for columnIndex,column in enumerate(line):
            if grid[lineIndex][columnIndex]=="X":
                cnv.create_line(+20+columnIndex*GAP,+20+lineIndex*GAP,-20+columnIndex*(GAP)+GAP,-20+lineIndex*(GAP)+GAP,fill='white',width=5,tags="s")
                cnv.create_line(-20+columnIndex*(GAP)+GAP,+20+lineIndex*GAP,20+columnIndex*(GAP),-20+lineIndex*(GAP)+GAP,fill='white',width=5,tags="s")
            elif grid[lineIndex][columnIndex]=="O":
                cnv.create_oval(columnIndex*GAP+GAP/2-RAYON,lineIndex*GAP+GAP/2-RAYON,columnIndex*GAP+GAP/2+RAYON,lineIndex*GAP+GAP/2+RAYON,width=5,tags="s")
