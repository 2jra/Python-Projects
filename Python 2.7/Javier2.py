# Creado por Juan Javier Rufino Arias.

import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
FPS = 30     #cuadros por segundos.
fpsClock = pygame.time.Clock()
pantalla = pygame.display.set_mode((640, 480))
fondo = pygame.image.load('Imagen/space.jpg')
fin = pygame.image.load('Imagen/gameover.jpg')
hero_posx = 320   #variable x de posicion inicial del protagonista.
pygame.key.set_repeat(50, 30) #Para cuando uno deje pisado una tecla se repita.



class Disparo:
    def __init__(self, xpos, ypos, ruta):
        self.imagen = pygame.image.load(ruta)
        self.x = xpos
        self.y = ypos
        self.ver()
        self.mover()
    def ver(self):
        pantalla.blit(self.imagen, (self.x, self.y))
    def mover(self):
        self.y -= 5



class Villano:
    def __init__(self, xpos, ypos):
        self.imagen = pygame.image.load('Imagen/alien.png')
        self.x = xpos
        self.y = ypos
        self.ver()
    def ver(self):
        pantalla.blit(self.imagen, (self.x, self.y))
        


class Villano2:
    def __init__(self, xpos, ypos):
        self.imagen = pygame.image.load('Imagen/ship.png')
        self.x = xpos
        self.y = ypos
        self.ver()
        self.mover()
    def ver(self):
        pantalla.blit(self.imagen, (self.x, self.y))
    def mover(self):
        self.y += 10
        

class Personaje:
    def __init__(self, xpos, ypos):
        self.imagen = pygame.image.load('Imagen/Hero.png')
        self.x = xpos
        self.y = ypos
        self.ver()
        self.mover()
    def ver(self):
        pantalla.blit(self.imagen, (self.x, self.y))
    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.x > 5:
            self.x -= 5
        if teclas[pygame.K_RIGHT] and self.x < 600:
            self.x += 5
            

def choque(pos1_x, pos1_y, pos2_x, pos2_y):
    if (pos1_x > pos2_x - 15) and (pos1_x < pos2_x + 15) and (pos1_y > pos2_y - 15) and (pos1_y < pos2_y + 15):
        return True
    else:
        return False
        

                   
heroe = Personaje(hero_posx, 450)
lista = []
pos_villano2 = randint(5, 600) #Para que el numero de la posicion salga aleatoriamente.
pos_villano = 5
villano2 = Villano2(pos_villano2, 50)
laser = Disparo(heroe.x, heroe.y, 'Imagen/Good_Laser.png')
laser_enemigo = Disparo(0, 480, 'Imagen/Bad_Laser.png')
activo = False

for x in range(10):       #Para entrar un conjuto de villanos en una lista.
    lista.append(Villano(pos_villano, 250))
    pos_villano += 40

while True:
    teclas = pygame.key.get_pressed()
    pantalla.blit(fondo, (0,0))
    heroe.ver()
    heroe.mover()
    villano2.ver()
    villano2.mover()

    if villano2.y == 480:    #Para que este villano vuelva aparecer en pantalla.
        villano2.y = 50
        villano2.x = randint(5, 600) #Para cuando aparezca de nuevo, su posicion en x sea aleatoria.

    if teclas[pygame.K_SPACE]:
        laser.x, laser.y = heroe.x, heroe.y
        activo = True


    if activo:
        laser.ver()
        laser.mover()
        if laser.y <= 0:
            activo = False

    
    for numero in range(len(lista)):     #Para visualizar los villanos dentro de la lista en la Pantalla.
        lista[numero].ver()


    if lista[0].x == 5:      #Desde aqui empieza las condiciones para mover los enemigos verdes.
        for numero in range(len(lista)):
            lista[numero].y -= 5


    if lista[len(lista)-1].x == 600:
        for numero in range(len(lista)):
            lista[numero].y += 5

    if lista[len(lista)-1].y == 400:
        for numero in range(len(lista)):
            lista[numero].x -= 5

    if lista[0].y == 50:
        for numero in range(len(lista)):
            lista[numero].x += 5          #Hasta aqui termina las condiciones para mover a los enemigos verdes.
 
    if laser_enemigo.y >= 480 and len(lista) > 0:      #Para que el laser enemigo aparezca aleatoriamente de un enemigo verde.
        laser_enemigo.x = lista[randint(0, len(lista) - 1)].x
        laser_enemigo.y = lista[0].y
		

    for enemigo in range(len(lista)):
        if choque(laser.x, laser.y, lista[enemigo].x, lista[enemigo].y):
            del lista[enemigo]
            break

    if choque(heroe.x, heroe.y, villano2.x, villano2.y):
        #pantalla.blit(fin, (0, 0))
        #pygame.time.wait(800)
        pygame.quit()
        sys.exit()

    if choque(heroe.x, heroe.y, laser_enemigo.x, laser_enemigo.y):
        #pantalla.blit(fin, (0, 0))
        #pygame.time.wait(800)
        pygame.quit()
        sys.exit()    

    if len(lista) == 0:
        #pantalla.blit(fin, (0, 0))
        #pygame.time.wait(800)
        pygame.quit()
        sys.exit()
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    laser_enemigo.ver()
    laser_enemigo.y += 5
            
    pygame.display.update()
    fpsClock.tick(FPS)
