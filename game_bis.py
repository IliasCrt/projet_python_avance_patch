import pygame as pg
import random as rd
import time
import math
import random

class Game:
    def __init__(self):
        self.L=[0]
        self.wait=0
        self.compteur=0
        self.z_p = 500
        self.dz_p = 0
        self.dx_p = 10
        self.x_p = 500
        self.projectile = False
        self.droit = True
        self.command_tir = False
        self.c_p = 1
        self.freaze = 0
        self.score_p = 10
        self.obstacle = [] # chaque obstacle est représenté par un tuple (position, hauteur et largeur), tous regroupés dans une liste
        self.background = pg.image.load("lieu1.png") 


    def update(self,t0,t,screen):
        #Choix de l'arrière plan
        screen.blit(self.background,(0,0))
        police = pg.font.Font(None, 100)

        #Fonction de génération des obstacles
        def obstacle(D):
            O = D
            v = min(400 + 100 * (t - t0 - 10) ** (3 / 4), 1000)
            return v
        #Evenements utilisateur
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.c_s += 1
                self.z += -30
                self.dz = self.v0
            if (event.type == pg.MOUSEBUTTONDOWN and event.button == 3) and self.c_p > 0 and self.command_tir == True:
                self.projectile = True
                self.c_p -= 1


        # Mise à jour de la position verticale de la boule  
        self.z = self.z - int((time.time() - t) * self.dz)
        self.dz = self.dz - int((time.time() - t) * self.a)

        # variables fantômes pour la commande de tir
        self.z_p = self.z
        self.dz_p = self.dz_p

        # La boule arrête de chuter au contact du sol
        if self.z >= 500 :
            self.dz = 0
            self.z = 500
            self.c_s = 0
            self.z_p = 500
            self.dz_p = 0

        pg.draw.circle(screen, (0,255,0), (500,self.z-self.r),self.r)

        for o in self.obstacle:
            o[0] += - int(v(t)*(time.time() - t))
            pg.draw.rect(screen,(255,0,0),(o[0] , 500 - o[1] , o[2] , o[1]))

        # Calcul et mise à jour du score
        self.Score += v(t)*(time.time() - t)

        #Supression des obstacles non visibles
        if len(self.obstacle) >= 1 and (self.obstacle[0][0] + self.obstacle[0][2] < 0 ):
            self.obstacle.pop(0)

        # Affichage du score
        texte = str(round(self.Score/100))
        texte_surface = police.render(texte, True, (0, 0, 0))
        coin_x, coin_y = 0, 0
        screen.blit(texte_surface, (coin_x, coin_y))

        # commande de tir
        # affichage de la commande et modalité de l'accesibilité
        if int(texte) >= 300 :
            self.command_tir = True
            if self.c_p > 0 :
                texte_p = " Vous avez {} shots !".format(str(self.c_p)) #affichage de l'accès à la commande de tir
                texte_surface = police.render(texte_p, True, (0, 0, 0))
                coin_x_p, coin_y_p = 400, 0
                screen.blit(texte_surface, (coin_x_p, coin_y_p))

                if self.droit == True : #afficher "clique droit" qu'une seule fois
                    texte_l = "(Clique droit)"
                    texte_surface = police.render(texte_l, True, (0, 0, 0))
                    coin_x_p, coin_y_p = 400, 50
                    screen.blit(texte_surface, (coin_x_p, coin_y_p))

                #La commande de tir est accessible à une fréquence donnée
                if self.c_p == 1 and self.freaze == 0 :
                    self.score_p += 150
                    self.freaze = 1 

            # A partir d'un certain score on passe de 1 tir à 2 tirs
            if self.c_p == 0 : 
                self.droit = False
                if  int(texte) < 500:
                    if int(texte) > self.score_p  :
                        self.c_p = 1
                        self.freaze = 0
                else :
                    if int(texte) > self.score_p :
                        self.c_p = 2
                        self.freaze = 0

        # génération du projectile
        if self.projectile == True :
            for o in self.obstacle :
                self.x_p = 500
                t_p = time.time()
                self.z_p = (self.z_p - int((t_p - t) * self.dz_p))
                self.dz_p = 0
                while self.x_p < 2000 :
                    self.x_p +=  int((time.time() - t) * 50) 
                    pg.draw.rect(screen, (255,0,255),(self.x_p , self.z_p - self.r  , 10 , 5))

                if (self.x_p >= o[0]) and (o[0] > 500) and (self.z_p >= 500 - o[1]) :
                    i = self.obstacle.index(o)
                    self.obstacle.pop(i)
                    self.z_p = self.z
                    self.dz_p = self.dz
                    self.projectile = False
                elif self.x_p >= 1200 :
                    self.projectile = False


        # Détection de la collision entre la boule et les obstacles
        for o in self.obstacle :
            for k in range(10):
                 if (x_a > o[0] and x_a <= o[0] + o[2]) and (y_b >= 500 - o[1]):
                    pg.draw.rect(screen,(255,0,0),(0 , 0 , 1200 , 500))
                    self.defeat = True

            #En cas de collision, on affiche un message de défaite
            if self.defeat == True :
                self.wait+=1
                police_2 = pg.font.Font(None, 600)
                texte = "LOSER !"
                texte_surface = police.render(texte, True, (0, 0, 0))
                coin_x, coin_y = 400,300 
                pg.draw.rect(screen,(255,0,0),(0 , 0 , 1080 , 720))
                screen.blit(texte_surface, (coin_x, coin_y))

            #Au bout d'un certain temps, on rénitialise les variables, et on retourne à l'accueil
                if self.wait == 70:
                    self.defeat = False
                    self.wait=0
                    self.L.append(self.Score)
                    self.c_s = 0
                    self.D = []
                    self.obstacle = []

                    #Retour à l'écran d'accueil
                    self.is_playing = False