from random import choice,randint
from upemtk import *
from time import *
import shutil
import sys
#le personnage Rockford (R),
# de la terre (G) que l’on peut creuser,
# un mur (W) infranchissable,
# un rocher (B),
# un rocher qui tombe (F),
# un diamant (D),
# un diamant qui tombe (T),
# la sortie (E),
# la sortie fermer (N).
#----------------------------------------------------VISUEL---------------------------------------------------------------------------------
def menu(largeur_fen,hauteur_fen): #Créer un petit menu de départ ou l'on peut selectionner les niveaux
    sauvegarde = 0
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black')
    with open('sauvegarde.txt','r') as f: #Si le fichier de sauvegarde est vide n'affiche pas le niveau "Continuer" car il n'existe pas
        fic = f.read()
        if fic!='':
            sauvegarde = 1
            rectangle(0.38*largeur_fen,0.65*hauteur_fen,0.64*largeur_fen,0.775*hauteur_fen,remplissage='grey50')
            texte(0.42*largeur_fen,0.69*hauteur_fen,'CONTINUER')
    rectangle(0.38*largeur_fen,0.125*hauteur_fen,0.64*largeur_fen,0.23*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.35*hauteur_fen,0.64*largeur_fen,0.475*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.50*hauteur_fen,0.64*largeur_fen,0.625*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.80*hauteur_fen,0.64*largeur_fen,0.925*hauteur_fen,remplissage='grey50')
    texte(0.40*largeur_fen,0.15*hauteur_fen,'BOULDER DASH')
    texte(0.43*largeur_fen,0.39*hauteur_fen,'AVENTURE')
    texte(0.40*largeur_fen,0.54*hauteur_fen,'MAP ALEATOIRE')
    texte(0.44*largeur_fen,0.84*hauteur_fen,'QUITTER')
    texte(0.15*largeur_fen,0.26*hauteur_fen,"Choisissez un mode de jeu, ou continuez votre partie :",'grey50')
    while True:
        x,y,clic = attente_clic()
        if 0.38*largeur_fen<x<0.64*largeur_fen and 0.35*hauteur_fen<y<0.475*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            return 1 #1 pour le niveau du fichier
        elif 0.38*largeur_fen<x<0.64*largeur_fen and 0.50*hauteur_fen<y<0.625*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            return 2 #2 pour un niveau aléatoire
        elif 0.38*largeur_fen<x<0.64*largeur_fen and 0.65*hauteur_fen<y<0.775*hauteur_fen and clic=='ClicGauche' and sauvegarde==1:
            efface_tout()
            return 3 #3 pour la sauvegarde
        elif 0.38*largeur_fen<x<0.64*largeur_fen and 0.80*hauteur_fen<y<0.925*hauteur_fen and clic=='ClicGauche':
            sys.exit()

def menu_aventure(largeur_fen,hauteur_fen): #Créer un menu pour choisir le niveau en mode aventure
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black')
    rectangle(0.38*largeur_fen,0.125*hauteur_fen,0.64*largeur_fen,0.23*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.35*hauteur_fen,0.64*largeur_fen,0.475*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.50*hauteur_fen,0.64*largeur_fen,0.625*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.65*hauteur_fen,0.64*largeur_fen,0.775*hauteur_fen,remplissage='grey50')
    texte(0.40*largeur_fen,0.15*hauteur_fen,'BOULDER DASH')
    texte(0.44*largeur_fen,0.39*hauteur_fen,'NIVEAU 1')
    texte(0.44*largeur_fen,0.54*hauteur_fen,'NIVEAU 2')
    texte(0.44*largeur_fen,0.69*hauteur_fen,'NIVEAU 3')
    while True:
        x,y,clic = attente_clic()
        if 0.38*largeur_fen<x<0.64*largeur_fen and 0.35*hauteur_fen<y<0.475*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            return 1 #Niveau 1
        elif 0.38*largeur_fen<x<0.64*largeur_fen and 0.51*hauteur_fen<y<0.625*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            return 2 #Niveau 2
        elif 0.38*largeur_fen<x<0.64*largeur_fen and 0.65*hauteur_fen<y<0.775*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            return 3 #Niveau 3

def menu_pause(largeur_fen,hauteur_fen,chrono):
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black')
    rectangle(0.38*largeur_fen,0.35*hauteur_fen,0.64*largeur_fen,0.475*hauteur_fen,remplissage='grey50')
    rectangle(0.38*largeur_fen,0.50*hauteur_fen,0.64*largeur_fen,0.625*hauteur_fen,remplissage='grey50')
    texte(0.43*largeur_fen,0.39*hauteur_fen,'CONTINUER')
    texte(0.44*largeur_fen,0.54*hauteur_fen,'QUITTER')
    temps_pause = time()
    while True:
        x,y,clic = attente_clic()
        if 0.38*largeur_fen<x<0.64*largeur_fen and 0.35*hauteur_fen<y<0.475*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            temps_pause = time() - temps_pause
            return 1,temps_pause #Niveau 1
        elif 0.38*largeur_fen<x<0.64*largeur_fen and 0.51*hauteur_fen<y<0.625*hauteur_fen and clic=='ClicGauche':
            efface_tout()
            return 2,temps_pause #Niveau 2

def explication_commandes(largeur_fen,hauteur_fen):
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black')
    texte(0.2*largeur_fen,0.1*hauteur_fen,'Utiliser les fleches ←↑→↓ pour vous deplacer','ORANGE')
    texte(0.2*largeur_fen,0.2*hauteur_fen,'Appuyer sur R pour recommencer le niveau','ORANGE')
    texte(0.2*largeur_fen,0.3*hauteur_fen,'Appuyer sur S pour sauvegarder la partie','ORANGE')
    texte(0.2*largeur_fen,0.4*hauteur_fen,'Appuyer sur D pour activer/desactiver le mode debug','ORANGE')
    texte(0.2*largeur_fen,0.5*hauteur_fen,'Appuyer sur ECHAP pour mettre le jeu en pause','ORANGE')
    texte(0.4*largeur_fen,0.7*hauteur_fen,'AMUSEZ-VOUS !!','ORANGE')

def affiche_terrain(terrain):
    #parcours tout le terrain a la recherche de R (Rockford) et les autres éléments afin de les affichers selon leur emplacement
    efface_tout()
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black') #Fond noir
    for i in range (len(terrain)):
        for j in range(len(terrain[0])):
                if terrain[i][j]=='R':
                    cercle(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/3.5,(largeur_fen//len(terrain[0]))/5,couleur='red',remplissage='red') #tête
                    cercle(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2.5,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/4,(largeur_fen//len(terrain[0]))/16,couleur='black',remplissage='black') #oeil gauche
                    cercle(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/1.65,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/4,(largeur_fen//len(terrain[0]))/16,couleur='black',remplissage='black') #oeil droit
                    ligne(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/3.5,j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1.2,epaisseur=3,couleur='red') #corps
                    ligne(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/3,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1.7,(j+1)*(largeur_fen//len(terrain[0]))-(largeur_fen//len(terrain[0]))/3,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1.7,epaisseur=3,couleur='red') #bras
                    ligne(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1.2,j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2.5,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1,epaisseur=3,couleur='red') #jambe gauche
                    ligne(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1.2,j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/1.65,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/1,epaisseur=3,couleur='red') #jambe droite
                elif terrain[i][j]=='W':
                    rectangle(j*(largeur_fen//len(terrain[0])),i*(hauteur_fen//len(terrain)),(j+1)*(largeur_fen//len(terrain[0])),(i+1)*(hauteur_fen//len(terrain)),couleur='black',remplissage='grey30')
                elif terrain[i][j]=='G':
                    rectangle(j*(largeur_fen//len(terrain[0])),i*(hauteur_fen//len(terrain)),(j+1)*(largeur_fen//len(terrain[0])),(i+1)*(hauteur_fen//len(terrain)),couleur='saddle brown',remplissage='saddle brown')
                elif terrain[i][j]=='B' or terrain[i][j]=='F':
                    cercle(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/2,i*(hauteur_fen//len(terrain))+(hauteur_fen//len(terrain))/2,(largeur_fen//len(terrain[0]))/2,remplissage='grey')
                elif terrain[i][j]=='D' or terrain[i][j]=='T':
                    polygone(points=((j*(largeur_fen//len(terrain[0]))+largeur_fen//len(terrain[0])/2,i*(hauteur_fen//len(terrain))),((j+1)*(largeur_fen//len(terrain[0])),i*(hauteur_fen//len(terrain))+hauteur_fen//len(terrain)/2),(j*(largeur_fen//len(terrain[0]))+largeur_fen//len(terrain[0])/2,(i+1)*(hauteur_fen//len(terrain))),(j*(largeur_fen//len(terrain[0])),i*(hauteur_fen//len(terrain))+hauteur_fen//len(terrain)/2)),remplissage='blue')
                elif terrain[i][j]=='E':
                    rectangle(j*(largeur_fen//len(terrain[0])),i*(hauteur_fen//len(terrain)),(j+1)*(largeur_fen//len(terrain[0])),(i+1)*(hauteur_fen//len(terrain)),couleur='green',remplissage='green')
                    texte(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/16,i*(hauteur_fen//len(terrain))+hauteur_fen//len(terrain)/4,'EXIT',couleur='black')
                elif terrain[i][j]=='N':
                    rectangle(j*(largeur_fen//len(terrain[0])),i*(hauteur_fen//len(terrain)),(j+1)*(largeur_fen//len(terrain[0])),(i+1)*(hauteur_fen//len(terrain)),couleur='red',remplissage='red')
                    texte(j*(largeur_fen//len(terrain[0]))+(largeur_fen//len(terrain[0]))/16,i*(hauteur_fen//len(terrain))+hauteur_fen//len(terrain)/4,'EXIT',couleur='black')

def affiche_chronometre(chrono) : #affiche visuellement le chrono
    texte(0.03 * largeur_fen,hauteur_fen + 10, 'Temps restant','grey')
    texte(0.1* largeur_fen,hauteur_fen + 50, chrono,'grey')

def affiche_diamants(diams_requis, diams) : #affiche visuellement le nombre de diamants requis
    x = diams_requis - diams
    if x > 0 :
        texte(0.85 * largeur_fen,hauteur_fen + 50, x,'grey')
    else :
        texte(0.85 * largeur_fen,hauteur_fen + 50, 0,'grey')
    texte(0.75*largeur_fen,hauteur_fen + 10,'Diamants requis','grey')

def affiche_score(score):
    texte(0.45 * largeur_fen,hauteur_fen + 50, score,'grey')
    texte(0.45  *largeur_fen,hauteur_fen + 10,'Score','grey')

def afficher_top5_scores():
    n = 0
    texte(largeur_fen//8,n+hauteur_fen//10,'Meilleurs scores','red')
    with open('Scores/Map'+str(niveau_aventure)+'_score.txt','r') as f:
        x = f.read()
        x = x.split('\n')
        for elem in x[:-1]:
            n+=hauteur_fen//15
            texte(largeur_fen//8,n+hauteur_fen//10,'Score : '+elem,'red')

def ecran_defaite(score):
    efface_tout()
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black') #Fond noir
    texte(largeur_fen//2,hauteur_fen//2,"Perdu!","red") #Affiche un message de défaite
    texte(largeur_fen//2.3,hauteur_fen//1.5,"Votre score:","red") #Affiche le score de fin
    texte(largeur_fen//1.6,hauteur_fen//1.5,score,"red")

def ecran_victoire(score,chrono):
    efface_tout()
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black') #Fond noir
    texte(largeur_fen//2,hauteur_fen//2,"Bravo!","red") #Affiche un message de victoire
    texte(largeur_fen//2.3,hauteur_fen//1.5,"Votre score:","red") #Affiche le score de fin
    texte(largeur_fen//1.6,hauteur_fen//1.5,score,"red")

#--------------------------------------------------FONCTIONNEMENT----------------------------------------------------------------------------------
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

#----------------------------------------------------MANIPULATION DE FICHIER-----------------------------------------------------------------------------
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

#--------------------------------------------------------MAIN-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    #Initialiser terrain et score
    largeur_fen = 1120  #Créer une fenetre
    hauteur_fen = 640
    cree_fenetre(largeur_fen, hauteur_fen + 100)
    explication_commandes(largeur_fen,hauteur_fen)
    attente_clic_ou_touche()
    if len(sys.argv) > 1 :
        fichier = sys.argv[1]
        terrain,temps_debut,diams_requis,diams = initialiser_terrain_sys(fichier)
    else :
        niveau = menu(largeur_fen,hauteur_fen)
        niveau_aventure = None
        if niveau==1:
            niveau_aventure = menu_aventure(largeur_fen,hauteur_fen)
            type_terrain=1
            terrain,temps_debut,diams_requis,diams,score,niveau_aventure = initialiser_terrain('Map'+str(niveau_aventure)+'.txt',type_terrain,niveau_aventure)

        elif niveau==2:
            type_terrain=2
            terrain_aleatoire('Map_aleatoire.txt')
            terrain,temps_debut,diams_requis,diams,score,niveau_aventure = initialiser_terrain('Map_aleatoire.txt',type_terrain,niveau_aventure)

        elif niveau==3:
            type_terrain=3
            terrain,temps_debut,diams_requis,diams,score,niveau_aventure = initialiser_terrain('sauvegarde.txt',type_terrain,niveau_aventure)
            diams_requis += diams
            if niveau_aventure == None:
                type_terrain = 2
            shutil.copy('sauvegarde.txt','continuer.txt') #Copie le fichier sauvegarde.txt dans le fichier continuer.txt afin de sauvegarder le début de la carte
                                                        #et en cas de sauvegarde puis de restart, le restart sera bien le debut du niveau lancé et non pas la dernière sauvegarde
    temps = 0
    temps_chute=time()
    tempstotal = time() + temps_debut
    debug=False
    direction=None
    while True:
        # Affichage terrain et physique du jeu
        affiche_terrain(terrain)
        if time()-temps_chute >0.2:
            chute_rocher_diamant(terrain, direction)
            temps_chute=time()
        sortie_active(terrain,diams,diams_requis)
        #Affichage du Timer, du score et du nombre de diamants requis
        tempstotal += temps  #ajoute au temps total du temps car un diamant a été attrapé
        temps = 0   #reinitialise le temps ajouter a 0 pour ne pas faire gagner du temps en boucle
        chrono = int(tempstotal - time())
        affiche_chronometre(chrono)
        affiche_diamants(diams_requis, diams)
        score = 500 * diams   #Chaque diamant vaut 500 points de score
        affiche_score(score)
        #Gestion des commandes
        ev=donne_evenement()
        type_ev=type_evenement(ev)
        if type_ev=="Touche":
            t=touche(ev)
            if t=="Right" or t=="Left" or t=="Up" or t=="Down":
                if debug==False:
                    for i in range(len(terrain)):
                        for j in range(len(terrain[0])):
                            if terrain[i][j]=='R' and (terrain[i+1][j]=='W' or terrain[i+1][j]=='N' or terrain[i+1][j]=='B') and t=='Down': #On ne peut pas descendre lorsqu'il y a un rocher/sortie fermer/Mur
                                t = None
                                direction = None
                            else:
                                direction=t
                    pousser(terrain,direction)
                    diams, temps = deplacement_Rockford(terrain,direction,diams,chrono)
            elif len(sys.argv) > 1 :
                if t=="r" :
                    terrain,temps_debut,diams_requis,diams = initialiser_terrain_sys(fichier)
                    tempstotal = time() + temps_debut
            elif t=="r" and type_terrain==1: #Bouton restart du mode de jeu aventure
                terrain,temps_debut,diams_requis,diams,score,niveau_aventure = initialiser_terrain('Map'+str(niveau_aventure)+'.txt',type_terrain,niveau_aventure)
                tempstotal = time() + temps_debut
            elif t=="r" and type_terrain==2: #Bouton restart du mode aléatoire
                 terrain,temps_debut,diams_requis,diams,score,niveau_aventure = initialiser_terrain('Map_aleatoire.txt',type_terrain,niveau_aventure)
                 tempstotal = time() + temps_debut
            elif t=="r" and type_terrain==3: #Bouton restart du mode continuer
                 terrain,temps_debut,diams_requis,diams,score,niveau_aventure = initialiser_terrain('continuer.txt',type_terrain,niveau_aventure)
                 diams_requis+=diams
                 tempstotal = time() + temps_debut
            elif t=="s": #Si on appuie sur "s", on effectue une sauvegarde
                sauvegarde(terrain,diams_requis,diams,chrono,score,type_terrain,niveau_aventure)
            elif t=="d": #Si on appuie sur "d", on lance le mode debug
                debug=not debug
            elif t=="Escape": #Si on appuie sur echap, met un ecran de pause
                choix,temps_pause = menu_pause(largeur_fen,hauteur_fen,chrono)
                if choix==1: #reprendre la partie
                    tempstotal += temps_pause
                else: #quitte la partie
                    ferme_fenetre()
                    sys.exit()
        #Gerer le mode debug
        elif (debug) and time()-temps_chute>0.19: #Mode debug fait bouger aléatoirement le personnage
            direction=choice(['Left', 'Right', 'Up', 'Down'])
            pousser(terrain,direction)
            diams,temps = deplacement_Rockford(terrain,direction,diams,chrono)
        #Met fin a la partie si la condition de victoire ou de défaite est vraie
        if perdu(terrain, chrono) or gagner(terrain) :
            break
        #Faire le rendu du terrain
        mise_a_jour()

    #Hors de la boucle while
    #effectue une derniere fois la vérification de chute afin d'eviter certains problemes de positionnement des rochers/diamants en fin de partie
    chute_rocher_diamant(terrain, direction)
    #Affiche le terrain a la fin de partie
    affiche_terrain(terrain)
    attente_clic_ou_touche()
    if perdu(terrain, chrono):
        ecran_defaite(score)
    else:
        score += chrono * 10 #Chaques secondes restantes donne 10 points de plus au score de fin
        ecran_victoire(score,chrono)
    if type_terrain!=2:
        sauvegarde_score(score,niveau_aventure) #Sauvegarde le score si il est parmi les 5 meilleurs sur le niveau
        afficher_top5_scores()
    attente_clic_ou_touche()
    ferme_fenetre()
