import os
import pygame
from constants import SZEROKOSC_EKRANU, WYSOKOSC_EKRANU
from platforma import Platforma
from kulka import Kulka

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.font.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")
czcionka = pygame.font.SysFont("Comic Sans MS", 24)

platforma = Platforma()
kulka = Kulka()
Zycia = 3

gra_dziala = True
while gra_dziala:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif event.type == pygame.QUIT:
            gra_dziala = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)

    platforma.aktualizuj()
    kulka.aktualizuj(platforma)
    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)

    tekst = czcionka.render(f"Życia: {Zycia}", False, (255, 0, 255))
    ekran.blit(tekst, (16,16))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()