from upemtk import *
from time import *
import sys

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


def affiche_terrain(terrain,largeur_fen,hauteur_fen):
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

def affiche_chronometre(chrono,largeur_fen,hauteur_fen) : #affiche visuellement le chrono
    texte(0.03 * largeur_fen,hauteur_fen + 10, 'Temps restant','grey')
    texte(0.1* largeur_fen,hauteur_fen + 50, chrono,'grey')

def affiche_diamants(diams_requis, diams,largeur_fen,hauteur_fen) : #affiche visuellement le nombre de diamants requis
    x = diams_requis - diams
    if x > 0 :
        texte(0.85 * largeur_fen,hauteur_fen + 50, x,'grey')
    else :
        texte(0.85 * largeur_fen,hauteur_fen + 50, 0,'grey')
    texte(0.75*largeur_fen,hauteur_fen + 10,'Diamants requis','grey')

def affiche_score(score,largeur_fen,hauteur_fen):
    texte(0.45 * largeur_fen,hauteur_fen + 50, score,'grey')
    texte(0.45  *largeur_fen,hauteur_fen + 10,'Score','grey')

def afficher_top5_scores(largeur_fen,hauteur_fen,niveau_aventure):
    n = 0
    texte(largeur_fen//8,n+hauteur_fen//10,'Meilleurs scores','red')
    with open('Scores/Map'+str(niveau_aventure)+'_score.txt','r') as f:
        x = f.read()
        x = x.split('\n')
        for elem in x[:-1]:
            n+=hauteur_fen//15
            texte(largeur_fen//8,n+hauteur_fen//10,'Score : '+elem,'red')

def ecran_defaite(score,largeur_fen,hauteur_fen):
    efface_tout()
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black') #Fond noir
    texte(largeur_fen//2,hauteur_fen//2,"Perdu!","red") #Affiche un message de défaite
    texte(largeur_fen//2.3,hauteur_fen//1.5,"Votre score:","red") #Affiche le score de fin
    texte(largeur_fen//1.6,hauteur_fen//1.5,score,"red")

def ecran_victoire(score,chrono,largeur_fen,hauteur_fen):
    efface_tout()
    rectangle(0,0,largeur_fen,hauteur_fen+100,remplissage='black') #Fond noir
    texte(largeur_fen//2,hauteur_fen//2,"Bravo!","red") #Affiche un message de victoire
    texte(largeur_fen//2.3,hauteur_fen//1.5,"Votre score:","red") #Affiche le score de fin
    texte(largeur_fen//1.6,hauteur_fen//1.5,score,"red")
