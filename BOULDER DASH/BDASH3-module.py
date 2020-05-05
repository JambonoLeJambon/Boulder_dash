#------------------------------------------------IMPORTS-------------------------------------------------------------------------------------------------------------------------------------------------------
from random import choice
from upemtk import *
from time import *
import shutil
import sys
from Fichier import *
from Fonctionnement import *
from Visuel import *
#-----------------------------------------------------MAIN--------------------------------------------------------------------------------------------------------------------------------------------------
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
        affiche_terrain(terrain,largeur_fen,hauteur_fen)
        if time()-temps_chute >0.2:
            chute_rocher_diamant(terrain, direction)
            temps_chute=time()
        sortie_active(terrain,diams,diams_requis)
        #Affichage du Timer, du score et du nombre de diamants requis
        tempstotal += temps  #ajoute au temps total du temps car un diamant a été attrapé
        temps = 0   #reinitialise le temps ajouter a 0 pour ne pas faire gagner du temps en boucle
        chrono = int(tempstotal - time())
        affiche_chronometre(chrono,largeur_fen,hauteur_fen)
        affiche_diamants(diams_requis, diams,largeur_fen,hauteur_fen)
        score = 500 * diams   #Chaque diamant vaut 500 points de score
        affiche_score(score,largeur_fen,hauteur_fen)
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
        if perdu(terrain,chrono) or gagner(terrain) :
            break
        #Faire le rendu du terrain
        mise_a_jour()

    #Hors de la boucle while
    #effectue une derniere fois la vérification de chute afin d'eviter certains problemes de positionnement des rochers/diamants en fin de partie
    chute_rocher_diamant(terrain, direction)
    #Affiche le terrain a la fin de partie
    affiche_terrain(terrain,largeur_fen,hauteur_fen)
    attente_clic_ou_touche()
    if perdu(terrain, chrono):
        ecran_defaite(score,largeur_fen,hauteur_fen)
    else:
        score += chrono * 10 #Chaques secondes restantes donne 10 points de plus au score de fin
        ecran_victoire(score,chrono,largeur_fen,hauteur_fen)
    if type_terrain!=2:
        sauvegarde_score(score,niveau_aventure) #Sauvegarde le score si il est parmi les 5 meilleurs sur le niveau
        afficher_top5_scores(largeur_fen,hauteur_fen,niveau_aventure)
    attente_clic_ou_touche()
    ferme_fenetre()
