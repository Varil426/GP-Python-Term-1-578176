import pygame
import random
import time
import os
from Jablko import Jablko

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Szerokość i wysokość ekranu
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608
Punkty = 0

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)

        tlo.blit(obraz, (i*32, j*32))

# Ustawienia
pygame.init()
pygame.font.init()
# Obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
# Obiekt czcionki
moja_czcionka = pygame.font.SysFont("Comic Sans MS", 24)

jablka = pygame.sprite.Group()
for i in range(1):
    jablko = Jablko()
    jablka.add(jablko)

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(tlo, (0,0))
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()
    zegar.tick(30)

time.sleep(3)
pygame.quit()
