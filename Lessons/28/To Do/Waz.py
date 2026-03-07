import pygame
import copy
from Kierunek import Kierunek
from Segment import Segment

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = self.kierunek
        self.ostatnia_pozycja = self.rect
        self.segmenty = []
        self.dodaj_segment = True

    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa = True
        if self.kierunek == Kierunek.GORA and kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if self.kierunek == Kierunek.DOL and kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if self.kierunek == Kierunek.PRAWO and kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False
        if self.kierunek == Kierunek.LEWO and kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False

        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(
            self.oryginalny_obraz, 
            self.kierunek.value * -90)
        
        self.ostatnia_pozycja = copy.deepcopy(self.rect)
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)

        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)

        if self.dodaj_segment:
            nowy_segment = Segment()
            nowa_pozycja = None
            if len(self.segmenty) > 0:
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
            nowy_segment.pozycja = nowa_pozycja
            self.segmenty.append(nowy_segment)
            self.dodaj_segment = False

    def rysuj_segmenty(self, ekran):
        for seg in self.segmenty:
            ekran.blit(seg.obraz, seg.pozycja)

    def jedz_jablko(self):
        self.dodaj_segment = True