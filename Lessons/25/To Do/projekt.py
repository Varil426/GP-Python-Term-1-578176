# dodanie modułu pygame
import pygame
from Element import NakrycieGlowy, Bron, Ubranie, Oczy

# dodanie modułu OS
import os

# Zmiana obecnej ścieżki pracy
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Utworzenie stałych
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load("images/background.png")
obraz_bazy_postaci = pygame.image.load("images/base.png")

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

pygame.font.init()
moja_czcionka = pygame.font.SysFont('Comic Sans MS', 30)

def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)

nakrycie_glowy = NakrycieGlowy()
oczy = Oczy()
ubranie = Ubranie()
bron = Bron()

gra_dziala = True

while gra_dziala:
    # Obsługa zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            elif zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            elif zdarzenie.key == pygame.K_w:
                oczy.wybierzNastepny()
            elif zdarzenie.key == pygame.K_e:
                ubranie.wybierzNastepny()
            elif zdarzenie.key == pygame.K_r:
                bron.wybierzNastepny()
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # Rysowanie
    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(obraz_bazy_postaci, (270, 130))
    ekran.blit(ubranie.wybranyObraz(), (270, 130))
    ekran.blit(oczy.wybranyObraz(), (270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(bron.wybranyObraz(), (270, 130))

    wypisz_tekst(ekran, f"[Q] Głowa: {nakrycie_glowy.wybrany}", (100, 100))
    wypisz_tekst(ekran, f"[W] Oczy: {oczy.wybrany}", (100, 140))
    wypisz_tekst(ekran, f"[E] Strój: {ubranie.wybrany}", (100, 180))
    wypisz_tekst(ekran, f"[R] Broń: {bron.wybrany}", (100, 220))
    
    pygame.display.flip()

    zegar.tick(30)
        

pygame.quit()