import sys
from random import randint

def initialiser_terrain_sys(fichier):
    ligne=[]
    terrain=[]
    temps=''
    diamant_req = ''
    score = ''
    it = 0
    with open(fichier,'r') as f: #Créer une matrice du terrain en lisant le fichier d'entree qui possede la carte en format texte
        x = f
        for elem in x:
            ligne = list(elem[:-1])
            terrain.append(ligne)
        for elm in terrain[0]:
            it += 1
            if elm == 's':
                break
            temps += elm
        for element in terrain[0][it:]:
            if element == 'd':
                break
            diamant_req += element
    diams = 0
    temps_debut = int(temps)
    diamant_requis = int(diamant_req)
    del terrain[0] #on delete terrain[0] car celui-ci correspond aux infos du temps et des diamants nécessaires
    return terrain,temps_debut,diamant_requis,diams

def initialiser_terrain(fichier,type_terrain,niveau_aventure):
    ligne=[]
    terrain=[]
    temps=''
    diamant_req = ''
    it = 0
    diams = 0
    points = 0
    niv_aventure = niveau_aventure
    with open(fichier,'r') as f: #Créer une matrice du terrain en lisant le fichier d'entree qui possede la carte en format texte
        for elem in f:
            ligne = list(elem[:-1])
            terrain.append(ligne)
        for elm in terrain[0]:
            it += 1
            if elm == 's':
                break
            temps += elm
        for element in terrain[0][it:]:
            if element == 'd':
                break
            diamant_req += element

    if type_terrain == 3:
        score = ''
        pts = ''
        if terrain[-1]==['1'] or terrain[-1]==['2'] or terrain[-1]==['3']: #Le niveau sauvegarder est soit une sauvegarde d'une sauvegarde soit un niveau de l'aventure car la derniere ligne est soit 1 2 ou 3 ce qui correspond au niveau du mode aventure sauvegarde
            for elem in terrain[-3]:
                if elem == 'd':
                    break
                score += elem
            diams = int(score)
            for elem in terrain[-2]:
                pts+=elem
            points = int(pts)
            for elem in terrain[-1]:
                niv_aventure = int(elem)
                del terrain[-3:] #On supprime les 3 dernières lignes car elles ne correspondent pas au terrain
        else:   #Si le niveau sauvegarder était un niveau aléatoire
            for elem in terrain[-2]:
                if elem == 'd':
                    break
                score += elem
            diams = int(score)
            for elem in terrain[-1]:
                pts+=elem
            points = int(pts)
            del terrain[-2:]

    temps_debut = int(temps)
    diamant_requis = int(diamant_req)
    del terrain[0] #on delete terrain[0] car celui-ci correspond aux infos du temps et des diamants nécessaires
    return terrain,temps_debut,diamant_requis,diams,points,niv_aventure

def terrain_aleatoire(fichier): #Créer un niveau aléatoire en 14x8 cases
    terrain1 = ''
    terrain2 = ''
    diams_totaux = 0
    terrain1 += str(randint(100,150))+'s '  #ajoute un temps qui varie entre 100 et 150 secondes pour le niveau
    for i in range(8):
        for j in range(14):
            if j==0 or j==13 or i==0 or i==7: #place des murs tout autour du niveau
                terrain2 += 'W'
            else:
                if i==2 and j==3:  #place rockford dans une place fixe
                    terrain2 +='R'
                elif i==6 and j==11: #place la sortie dans une place fixe
                    terrain2 += 'E'
                else:
                    alea = randint(1,10)
                    if alea==3:
                        terrain2+='B' # 1/10 Rochers
                    elif alea==2:
                        terrain2+='D' # 1/10 Diamants
                        diams_totaux += 1
                    elif alea==1:
                        terrain2+='.' # 1/10 cases vides
                    else:
                        terrain2+='G' # 7/10 cases de terre
        terrain2+='\n'
    terrain1 += str(diams_totaux//2) + 'd\n'
    terrain = terrain1 + terrain2
    with open(fichier,"w") as f:
        f.write(terrain)  #ecrit la map aleatoire dans un fichier qui va ensuite etre lu par la fonction initialiser_terrain

def sauvegarde(terrain,diams_requis,diams,chrono,score,type_terrain,niveau_aventure): #Créer un fichier de sauvegarde de la partie actuelle
    terrain_str = ''
    terrain_str += str(chrono) + 's '
    terrain_str += str(diams_requis-diams) + 'd \n'
    for i in range(len(terrain)):
        for j in range(len(terrain[0])):
            x = terrain[i][j]
            terrain_str += x
        terrain_str += '\n'
    terrain_str += str(diams) + 'd\n'
    terrain_str += str(score) + '\n'
    if type_terrain!=2:
        terrain_str+=str(niveau_aventure)+'\n'
    with open('sauvegarde.txt','w') as f: # Ecrit la sauvegarde de la partie dans le fichier sauvegarde
        f.write(terrain_str)

def sauvegarde_score(score,niveau_aventure):
    liste_score = []
    score_str = ''
    with open('Scores/Map'+str(niveau_aventure)+'_score.txt','r') as f:
        x = f.read()
        x = x.split('\n')
        for elem in x:
            if len(liste_score) != 5:
                liste_score.append(int(elem)) #On créer une liste des scores actuel
    liste_score.append(score) #On rajoute le score a la liste des scores
    liste_score.sort(reverse=True) #On tri par ordre décroissant les scores
    del liste_score[5] # On supprime le dernier score (le 6eme) afin qu'il reste un top 5
    for elem in liste_score:
        score_str+=str(elem)+'\n'
    with open('Scores/Map'+str(niveau_aventure)+'_score.txt','w') as f:
        f.write(score_str)
