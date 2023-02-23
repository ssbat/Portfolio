from Affichage import *
from  gamerules import *

class Node:
    
    def __init__(self,state,father):
        self.State=state
    


class IA:
    def draw(self,grid:list)->bool:
        s=0
        for i in grid:
            s+=i.count("_")
        if (s==0):
            return True
        return False
        

    def MinMax(self,grid,ISMAX):
        if (ISMAX):
            v=-1000000
            l,c=(NONE,NONE)
            for l2,c2 in coups_possible(grid):
                grid[l2][c2]="X"
                score=max(v,self.minvaleur(grid,PROFONDEUR,True,-10000000,+10000000))
                grid[l2][c2]='_'
                if(score>v):
                    l,c=l2,c2
                    v=score   
            print("Finale",v)         
            return l,c
        else:
            v=-1000000
            l,c=(NONE,NONE)
            for l2,c2 in coups_possible(grid):
                grid[l2][c2]="O"
                score=max(v,self.minvaleur(grid,PROFONDEUR,ISMAX,-10000000,+10000000))
                grid[l2][c2]='_'
                # print(score)
                if(score>v):
                    l,c=l2,c2
                    v=score  
                print("Finale",v)         
 
            return l,c
    

    def maxvaleur(self,grid,profondeur,ISMAX,alpha,beta):
        if (ISMAX):
            if  victoire(grid,"X") or draw(grid)or victoire(grid,"O") or profondeur==0:
                return eval(grid,"X",profondeur)

            else:
                v=-1000000
                for l,c in coups_possible(grid):
                    grid[l][c]="X"
                    v=max(v,self.minvaleur(grid,profondeur-1,ISMAX,alpha,beta))
                    grid[l][c]='_'
                    if v >= beta:
                            return v
                    if v > alpha:
                            alpha = v
                return v
        else:
            if  victoire(grid,"O") or draw(grid) or victoire(grid,"X") or profondeur==0:
                return eval(grid,"O",profondeur)

            else:
                v=-1000000
                for l,c in coups_possible(grid):
                    grid[l][c]="O"
                    v=max(v,self.minvaleur(grid,profondeur-1,ISMAX,alpha,beta))
                    grid[l][c]='_'
                    if v >= beta:
                            return v
                    if v > alpha:
                            alpha = v
                return v



    def minvaleur(self,grid,profondeur,ISMAX,alpha,beta):
        if(ISMAX):
            if  victoire(grid,"X") or draw(grid) or victoire(grid,"O") or profondeur==0:
                return eval(grid,"X",profondeur)
            else:
                v=1000000
                for l,c in coups_possible(grid):
                    grid[l][c]="O"
                    v=min(v,self.maxvaleur(grid,profondeur-1,ISMAX,alpha,beta))
                    grid[l][c]='_'
                    if  v<= alpha:
                            return  v 
                    if  v<beta:
                        beta =  v 
                return v
        else:
            
            if  victoire(grid,"O") or draw(grid) or victoire(grid,"X") or profondeur==0 :
                return eval(grid,"O",profondeur)
            else:
                v=1000000
                for l,c in coups_possible(grid):
                    grid[l][c]="X"
                    v=min(v,self.maxvaleur(grid,profondeur-1,ISMAX,alpha,beta))
                    grid[l][c]='_'
                    if  v<= alpha:
                            return  v 
                    if  v<beta:
                        beta =  v 
                return v
















    # def MinMax(self,grid,ISMAX):
    #     if (ISMAX):
    #         v=-1000000
    #         l,c=(NONE,NONE)
    #         for l2,c2 in coups_possible(grid):
    #             grid[l2][c2]="X"
    #             score=max(v,self.minvaleur(grid,PROFONDEUR,True))
    #             grid[l2][c2]='_'
    #             if(score>v):
    #                 l,c=l2,c2
    #                 v=score   
    #         print("Finale",v)         
    #         return l,c
    #     else:
    #         v=-1000000
    #         l,c=(NONE,NONE)
    #         for l2,c2 in coups_possible(grid):
    #             grid[l2][c2]="O"
    #             score=max(v,self.minvaleur(grid,PROFONDEUR,ISMAX))
    #             grid[l2][c2]='_'
    #             # print(score)
    #             if(score>v):
    #                 l,c=l2,c2
    #                 v=score   
    #         return l,c
    

    # def maxvaleur(self,grid,profondeur,ISMAX):
    #     if (ISMAX):
    #         if  victoire(grid,"X") or draw(grid)or victoire(grid,"O") or profondeur==0:
    #             return eval(grid,"X",profondeur)

    #         else:
    #             v=-1000000
    #             for l,c in coups_possible(grid):
    #                 grid[l][c]="X"
    #                 v=max(v,self.minvaleur(grid,profondeur-1,ISMAX))
    #                 grid[l][c]='_'
    #             return v
    #     else:
    #         if  victoire(grid,"O") or draw(grid) or victoire(grid,"X") or profondeur==0:
    #             return eval(grid,"O",profondeur)

    #         else:
    #             v=-1000000
    #             for l,c in coups_possible(grid):
    #                 grid[l][c]="O"
    #                 v=max(v,self.minvaleur(grid,profondeur-1,ISMAX))
    #                 grid[l][c]='_'
    #             return v



    # def minvaleur(self,grid,profondeur,ISMAX):
    #     if(ISMAX):
    #         if  victoire(grid,"X") or draw(grid) or victoire(grid,"O") or profondeur==0:
    #             return eval(grid,"X",profondeur)
    #         else:
    #             v=1000000
    #             for l,c in coups_possible(grid):
    #                 grid[l][c]="O"
    #                 v=min(v,self.maxvaleur(grid,profondeur-1,ISMAX))
    #                 grid[l][c]='_'
    #             return v
    #     else:
            
    #         if  victoire(grid,"O") or draw(grid) or victoire(grid,"X") or profondeur==0 :
    #             return eval(grid,"O",profondeur)
    #         else:
    #             v=1000000
    #             for l,c in coups_possible(grid):
    #                 grid[l][c]="X"
    #                 v=min(v,self.maxvaleur(grid,profondeur-1,ISMAX))
    #                 grid[l][c]='_'
    #             return v
