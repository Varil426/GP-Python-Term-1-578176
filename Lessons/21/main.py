class Samochod:
    # marka = ""
    # model = ""
    # typSilnika = ""
    # mocKM = 0
    licznik = 0

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typSilnika, self.mocKM)
        print(f"Wszystkich samochodów jest: {Samochod.licznik}")

    def __init__(self, marka, model, typSilnika, mocKM):
        print("Tworzenie obiektu Samochod")
        self.marka = marka
        self.model = model
        self.typSilnika = typSilnika
        self.mocKM = mocKM
        Samochod.licznik += 1

s1 = Samochod("Pagani", "Zonda 760 Venti", "Benza", 760)
# s1.marka = "Pagani"
# s1.model = "Zonda 760 Venti"
# s1.typSilnika = "Benza"
# s1.mocKM = 760
s1.wyswietl()

s2 = Samochod("BMW", "E36", "Benza", 102)
s2.wyswietl()

s3 = Samochod("Ferrari", "Bonzo", "Benza", 660)
s3.wyswietl()