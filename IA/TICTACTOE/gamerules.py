def coups_possible(grid):
    liste=[]
    for lineIndex,line in enumerate(grid):
        for columnIndex,column in enumerate(line):
            if(grid[lineIndex][columnIndex]=="_"):
                liste.append((lineIndex,columnIndex))
    return liste
def eval(grid,player,profondeur):
    if(victoire(grid,player)):
        return 10+profondeur*6
            
    if (player=="O"):
        if  (victoire(grid,"X")):
            return -10-profondeur*6
        for i in grid:
            if i.count("X")==2 and i.count("_")==1:
                return -7-profondeur*6
            if i.count("O")==2 and i.count("_")==1:
                return 7+profondeur*6
            else:
                if (grid[0][0]==grid[1][1]=="X" and grid[2][2]=="_" )or (grid[0][0]==grid[2][2]=="X" and grid[1][1]=="_") or (grid[1][1]==grid[2][2]=="X" and grid[0][0]=="_"):
                  return -7-profondeur*6
                if (grid[0][2]==grid[1][1]=="X" and grid[2][0]=="_" )or (grid[0][2]==grid[2][0]=="X" and grid[1][1]=="_") or (grid[1][1]==grid[2][0]=="X" and grid[0][2]=="_"):
                      return -7-profondeur*6
                if (grid[0][0]==grid[1][1]=="O" and grid[2][2]=="_" )or (grid[0][0]==grid[2][2]=="O" and grid[1][1]=="_") or (grid[1][1]==grid[2][2]=="O" and grid[0][0]=="_"):
                      return 7+profondeur*6
                if (grid[0][2]==grid[1][1]=="O" and grid[2][0]=="_" )or (grid[0][2]==grid[2][0]=="O" and grid[1][1]=="_") or (grid[1][1]==grid[2][0]=="O" and grid[0][2]=="_"):
                    return 7+profondeur*6
    else:
        if  (victoire(grid,"O")):#na2es
            return -10-profondeur*6
        for i in grid:
            if i.count("O")==2 and i.count("_")==1:
                return -7-profondeur*6
            if i.count("X")==2 and i.count("_")==1:
                return 7+profondeur*6
            else:
                if (grid[0][0]==grid[1][1]=="O" and grid[2][2]=="_" )or (grid[0][0]==grid[2][2]=="O" and grid[1][1]=="_") or (grid[1][1]==grid[2][2]=="O" and grid[0][0]=="_"):
                  return -7-profondeur*6
                if (grid[0][2]==grid[1][1]=="O" and grid[2][0]=="_" )or (grid[0][2]==grid[2][0]=="O" and grid[1][1]=="_") or (grid[1][1]==grid[2][0]=="O" and grid[0][2]=="_"):
                      return -7-profondeur*6
                if (grid[0][0]==grid[1][1]=="X" and grid[2][2]=="_" )or (grid[0][0]==grid[2][2]=="X" and grid[1][1]=="_") or (grid[1][1]==grid[2][2]=="X" and grid[0][0]=="_"):
                      return 7+profondeur*6
                if (grid[0][2]==grid[1][1]=="X" and grid[2][0]=="_" )or (grid[0][2]==grid[2][0]=="X" and grid[1][1]=="_") or (grid[1][1]==grid[2][0]=="X" and grid[0][2]=="_"):
                    return 7+profondeur*6
    if draw(grid):
        return 0
    return 0

    
def victoire(grid,player):
    liste_cases=listeCases(grid,player)#les possibilite pour x ou pour O
    listel=[]
    listec=[]
    for nl,nc in liste_cases:
        listec.append(nc)#liste des coordonne x
        listel.append(nl)#liste des coordonne y
    if len(liste_cases)>=3:
        for i in range(len(listel)):
            if listel.count(listel[i])==3:#victoir verticale
                
                return True
            if listec.count(listec[i])==3:#victoire horozontale 
                return True
        #victoire oblique
        if(grid[0][0]==grid[1][1]==grid[2][2]==player or grid[0][2]==grid[1][1]==grid[2][0]==player):
            return True
    return False

def coups_possible(grid):
    liste=[]
    for lineIndex,line in enumerate(grid):
        for columnIndex,column in enumerate(line):
            if(grid[lineIndex][columnIndex]=="_"):
                liste.append((lineIndex,columnIndex))
    return liste

def listeCases(grid,player):
    liste=[]
    for lineIndex,line in enumerate(grid):
        for columnIndex,column in enumerate(line):
            if (grid[lineIndex][columnIndex]==player):
                liste.append((lineIndex,columnIndex))
    return liste


def draw(grid:list)->bool:
    s=0
    for i in grid:
        s+=i.count("_")
    if (s==0):
        return True
    return False
def valide(grid,l,c)->bool:
    if grid[l][c]=="_":
        return True
    return False


    