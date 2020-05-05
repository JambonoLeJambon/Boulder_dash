def deplacement_Rockford(terrain,direction,diams,chrono): #permet de déplacer Rockford dans la liste
    temps = 0
    if direction == 'Up':
        for i in range(len(terrain)):  #parcours la liste
            for j in range(len(terrain[0])):
                if terrain[i][j]=='R' and (terrain[i-1][j]=='.' or terrain[i-1][j]=='G' or terrain[i-1][j]=='E'):  #Vérifie que Rockford puisse se déplacer en haut
                    terrain[i][j]='.'       #Remplace l'ancienne position de Rockford par une case vide
                    terrain[i-1][j]='R'     #Ajoute Rockford dans la case de la direction voulue

                elif terrain[i][j]=='R' and terrain[i-1][j]=='D': #vérifie si la case possède un diamant
                    terrain[i][j]='.'
                    terrain[i-1][j]='R'
                    diams += 1
                    temps += 5

    elif direction == 'Down':
        for i in range(len(terrain)-1,-1,-1):
            for j in range(len(terrain[0])):
                if terrain[i][j]=='R' and (terrain[i+1][j]=='.' or terrain[i+1][j]=='G' or terrain[i+1][j]=='E'):
                    terrain[i][j]='.'
                    terrain[i+1][j]='R'

                elif terrain[i][j]=='R' and terrain[i+1][j]=='D' : #vérifie si la case possède un diamant
                    terrain[i][j]='.'
                    terrain[i+1][j]='R'
                    diams += 1
                    temps += 5

    if direction == 'Left':
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                if terrain[i][j]=='R' and (terrain[i][j-1]=='.' or terrain[i][j-1]=='G' or terrain[i][j-1]=='E'):
                    terrain[i][j]='.'
                    terrain[i][j-1]='R'

                elif terrain[i][j]=='R' and terrain[i][j-1]=='D' :
                    terrain[i][j]='.'
                    terrain[i][j-1]='R'
                    diams += 1
                    temps += 5

    elif direction == 'Right':
        for i in range(len(terrain)):
            for j in range(len(terrain[0])-1,-1,-1):
                if terrain[i][j]=='R' and (terrain[i][j+1]=='.' or terrain[i][j+1]=='G' or terrain[i][j+1]=='E'):
                    terrain[i][j]='.'
                    terrain[i][j+1]='R'

                elif terrain[i][j]=='R' and terrain[i][j+1]=='D':
                    terrain[i][j]='.'
                    terrain[i][j+1]='R'
                    diams += 1
                    temps += 5

    return diams, temps

def pousser(terrain,direction):
    if direction == 'Left':
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
#La case actuelle est Rockford et la case d'après est un rocher et la case encore après est vide
                if terrain[i][j]=='R' and terrain[i][j-1]=='B' and terrain[i][j-2]=='.':
                    terrain[i][j]='.'   #remplace la première case par du vide
                    terrain[i][j-1]='R' #remplace la deuxieme case par du vide
                    terrain[i][j-2]='B' #remplace la troisieme case par du vide


    elif direction == 'Right':
        for i in range(len(terrain)):
            for j in range(len(terrain[0])-1,-1,-1):
                if terrain[i][j]=='R' and terrain[i][j+1]=='B' and terrain[i][j+2]=='.':
                    terrain[i][j]='.'
                    terrain[i][j+1]='R'
                    terrain[i][j+2]='B'

def chute_rocher_diamant(terrain, direction):
    for i in range(len(terrain)-1,-1,-1):
        for j in range(len(terrain[0])):
            if terrain[i][j]=='B' and terrain[i+1][j]=='.':  #si un rocher est au-dessus d'une case vide
                terrain[i][j]='F'  #transforme le rocher en rocher qui tombe 'F'=> Falling

            elif terrain[i][j]=='B' and (terrain[i+1][j]=='B' or terrain[i+1][j]=='D')  and terrain[i][j+1]=='.' and terrain[i+1][j+1]=='.' : # gère la chute latéral du rocher quand un rocher est sur un autre rocher/diamant et que la case sur le coté droit est vide
                terrain[i][j]='.'
                terrain[i][j+1]='B'

            elif terrain[i][j]=='B' and (terrain[i+1][j]=='B' or terrain[i+1][j]=='D')  and terrain[i][j-1]=='.' and terrain[i+1][j-1]=='.':  # gère la chute latéral du rocher quand un rocher est sur un autre rocher/diamant et que la case sur le coté gauche est vide
                terrain[i][j]='.'
                terrain[i][j-1]='B'

            elif terrain[i][j]=='D' and terrain[i+1][j]=='.'  :  #si un diamant est au-dessus d'une case vide
                terrain[i][j]='T'    #transforme le diamant en diamant qui tombe 'T'=> Tomber

            elif terrain[i][j]=='D' and (terrain[i+1][j]=='B' or terrain[i+1][j]=='D')  and terrain[i][j+1]=='.' and terrain[i+1][j+1]=='.' : # gère la chute latéral du diamant quand un diamant est sur un autre rocher/diamant et que la case sur le coté droit est vide
                terrain[i][j]='.'
                terrain[i][j+1]='D'

            elif terrain[i][j]=='D' and (terrain[i+1][j]=='B' or terrain[i+1][j]=='D')  and terrain[i][j-1]=='.' and terrain[i+1][j-1]=='.':  # gère la chute latéral du diamant quand un rocher est sur un autre rocher/diamant et que la case sur le coté gauche est vide
                terrain[i][j]='.'
                terrain[i][j-1]='D'

            elif terrain[i][j]=='R' and (terrain[i-1][j]=='F' or terrain[i-1][j]=='T') :  #Rockford se fait ecraser par un rocher/diamant si il est en dessous de celui-ci et si il descend d'une case
                terrain[i][j]='.'

            elif terrain[i][j]=='F' and (terrain[i+1][j]=='.' or terrain[i+1][j]=='R'): #Le rocher qui tombe continue de tomber si il y a du Vide ou Rockford en dessous
                terrain[i][j]='.'
                terrain[i+1][j]='F'

            elif terrain[i][j]=='F' and terrain[i+1][j]!='.' and terrain[i+1][j]!='R': #Le rocher qui tombe arrete de tomber si il y a une case autre que du vide et Rockford en dessous
                terrain[i][j]='B'

            elif terrain[i][j]=='T' and (terrain[i+1][j]=='.' or terrain[i+1][j]=='R'): #Le rocher qui tombe continue de tomber si il y a du Vide ou Rockford en dessous
                terrain[i][j]='.'
                terrain[i+1][j]='T'

            elif terrain[i][j]=='T' and terrain[i+1][j]!='.' and terrain[i+1][j]!='R': #Le rocher qui tombe arrete de tomber si il y a une case autre que du vide et Rockford en dessous
                terrain[i][j]='D'

def perdu(terrain, chrono):  #Vérifie si la partie est perdue
    case = 0
    for i in range(len(terrain)):
        for j in range(len(terrain[0])):
            if terrain[i][j]!='R':
                case += 1
                if case == (len(terrain)*len(terrain[0])) or chrono == 0 : #Si aucune case n'est Rockford alors vous avez perdu
                    return True

def gagner(terrain):
    case = 0
    for i in range(len(terrain)):
        for j in range(len(terrain[0])):
            if terrain[i][j]!='E' and terrain[i][j]!='N':
                case += 1
                if case == (len(terrain)*len(terrain[0])): #Si il n'y a plus de case exit alors vous êtes dessus donc vous avez gagnez
                    return True

def sortie_active(terrain,diams,diams_requis):
    if diams<diams_requis:
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                if terrain[i][j]=='E':
                    terrain[i][j]='N' #bloque la sortie si on a pas les diamants requis

    else:
        for i in range(len(terrain)):
            for j in range(len(terrain[0])):
                if terrain[i][j]=='N':
                    terrain[i][j]='E' #debloque la sortie quand on a les diamants requis
