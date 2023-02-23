import time
from Affichage import *
from IA import *
from  gamerules import *


def generation(event,cnv,player_turn,grid,label:Label,ISMAX=False):
    print("x=",event.x//200)#colonne
    print("y=",event.y//200)#ligne
    c=event.x//200
    l=event.y//200
    if valide(grid,l,c):
        symbol=player_turn_symbol(player_turn)
        grid[l][c]=symbol
        draw_grid(cnv,grid)
        player_turn[0]+=1
        if (victoire(grid,symbol)):
            print("Victoire",symbol)
            label.config(text="Victoire PLAYER")
        elif draw(grid):
            label.config(text="DRAW")
        else:
            ia=IA()
            symbol=player_turn_symbol(player_turn)

            l2,c2=ia.MinMax(grid,ISMAX)
            grid[l2][c2]=symbol
            if (victoire(grid,symbol)):
                print("Victoire",symbol)
                label.config(text="Victoire IA")
            elif draw(grid):
                label.config(text="DRAW")
            draw_grid(cnv,grid)

            player_turn[0]+=1
    else:
        print("Invalide")



#IA START
def generation2(cnv,player_turn,grid,label:Label):

            ia=IA()
            symbol=player_turn_symbol(player_turn)

            l2,c2=ia.MinMax(grid,TRUE)
            # print(l2,c2,"COUP IA")
            grid[l2][c2]=symbol
            if (victoire(grid,symbol)):
                print("Victoire",symbol)
                label.config(text="Victoire IA")
            draw_grid(cnv,grid)

            player_turn[0]+=1
            cnv.bind("<Button-1>",lambda event: generation(event,cnv,player_turn,grid,label,TRUE))




#Player 1 vs Player 2
def generation3(event,cnv,player_turn,grid,label:Label):
    print("x=",event.x//200)#colonne
    print("y=",event.y//200)#ligne
    c=event.x//200
    l=event.y//200
    if valide(grid,l,c):
        symbol=player_turn_symbol(player_turn)
        grid[l][c]=symbol
        draw_grid(cnv,grid)
        if (victoire(grid,symbol)):
            print("Victoire",symbol)
            if(player_turn[0]%2==0):
                label.config(text="Victoire PLAYER 1")
            else:
                label.config(text="Victoire PLAYER 2")

            
        elif draw(grid):
            label.config(text="DRAW")
        player_turn[0]+=1



def player_turn_symbol(player_turn)->str:
    if (player_turn[0]%2==0):
        return "X"
    return "O"


def IAVSIA(cnv:Canvas,grid,player_turn,label):
    finished=False
    while not finished:
            i=0
            for i in range(100000):
                i=i
            ia=IA()
            symbol=player_turn_symbol(player_turn)

            l2,c2=ia.MinMax(grid,ISMAX=TRUE)
            grid[l2][c2]="X"
            draw_grid(cnv,grid)
            cnv.update()
            i=0
            #like a sleep pour gasbiller de temps
            for i in range(100000):
                i=i
            
            if (victoire(grid,symbol)):
                print("Victoire",symbol)
                label.config(text="Victoire IA")
                finished=True
                # break
            elif draw(grid):
                label.config(text="DRAW")
                finished=True
            else:
                time.sleep(2)
                player_turn[0]+=1
                
                ia2=IA()
                symbol=player_turn_symbol(player_turn)
                l2,c2=ia2.MinMax(grid,ISMAX=FALSE)
                grid[l2][c2]="O"
                draw_grid(cnv,grid)
                cnv.update()
                k=0
                for k in range(1000000):
                    k=k
                if (victoire(grid,symbol)):
                    print("Victoire",symbol)
                    label.config(text="Victoire IA")
                    finished=True
                if draw(grid):
                    label.config(text="DRAW")
                    finished=True
                player_turn[0]+=1
        