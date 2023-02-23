from tkinter import*
from Constante import *
from Affichage import*
from Play import*
from Buttonactions import *
import os
import sys
def resource_path(relative):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative)

root=Tk()
root.title("TicTacToe")
root.wm_attributes('-transparentcolor', '#ab23ff')

path1=resource_path("test3.png")
path2=resource_path("test4.png")
bg3 = PhotoImage(file=path2)
bgimg = PhotoImage(file = path1)

label1 = Label(root, image=bg3)
label1.place(x=500, y=0)
root.minsize(WIDTH+EXTRAWIDTH,HEIGHT)

label=Label(root,text="Enter Game Mode",width=15,height=2,fg="white",font=('Helvetica bold', 15),bg="black")
label.place(x=WIDTH+EXTRAWIDTH//3,y=20)



cnv=Canvas(root,width=WIDTH,height=HEIGHT)
cnv.create_image(0, 0,image=bgimg, anchor=NW)
cnv.pack()
cnv.place(x=0,y=0)

grid=[["_" for i in range(NBCOLUMN)] for j in range(NBCOLUMN)]
player_turn=[0]
button=Button(root,text="Reset",width=15,height=2,command=lambda:Reset(cnv,grid,player_turn,label)).place(x=WIDTH+40,y=HEIGHT//3)
button=Button(root,text="IA CONTRE IA",width=15,height=2,command=lambda:IAVSIA(cnv,grid,player_turn,label)).place(x=WIDTH+EXTRAWIDTH//2+40,y=HEIGHT//3)

def start():
    Reset(cnv,grid,player_turn,label)
    cnv.bind("<Button-1>",lambda event: generation(event,cnv,player_turn,grid,label))
    label.config(text="PLAYING")

def start2():
    Reset(cnv,grid,player_turn,label)
    generation2(cnv,player_turn,grid,label)
    label.config(text="PLAYING")
def start3():
    Reset(cnv,grid,player_turn,label)
    cnv.bind("<Button-1>",lambda event: generation3(event,cnv,player_turn,grid,label))
    label.config(text="PLAYING")


button=Button(root,text="YOU CONTRE IA and YOU START",width=30,height=2,command=start).place(x=WIDTH+EXTRAWIDTH//4,y=HEIGHT//2)
button=Button(root,text="YOU CONTRE IA and The IA STARTS",width=30,height=2,command=start2).place(x=WIDTH+EXTRAWIDTH//4,y=HEIGHT//2+70)
button=Button(root,text="Player 1 vs Player 2",width=30,height=2,command=start3).place(x=WIDTH+EXTRAWIDTH//4,y=HEIGHT//2+140)

draw_grid(cnv,grid)
create_cnv(cnv)

root.mainloop()