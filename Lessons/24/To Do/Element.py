import pygame

class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka):
        super().__init__()
        self.obraz = pygame.image.load(sciezka)

class Element():
    def __init__(self, typ):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1, 4):
            sciezka = f"images/{typ}{i}.png"
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)
    
    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany >= len(self.lista_obrazow):
            self.wybrany = 0

    def wybranyObraz(self):
        return self.lista_obrazow[self.wybranyObraz].obraz
    
# TODO Stworzyć klasy NakrycieGlowy itd.