class Uzytkownik:
    imie = ""
    nazwisko = ""
    wiek = 0

    def wyswietl(self):
        print(self.imie, self.nazwisko)
        if self.wiek >= 18:
            print(f"{self.imie} ma {self.wiek} lat, czyli jest pełnoletni")
        else:
            print(f"{self.imie} ma {self.wiek} lat, czyli nie jest pełnoletni")

    def zmien_wiek(self, nowy_wiek):
        if (nowy_wiek < 0):
            print("Wiek ujemny - pomijam")
            return
        self.wiek = nowy_wiek