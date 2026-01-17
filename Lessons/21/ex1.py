"""
Stwórz klasy: `Kolo` i `Kwadrat`.
Klasy powinny przechowywać informację o figurze (promień lub bok).
Dodaj metody do obliczania pola i obwodu - powinny zwracać wartości.
Pamiętaj, aby stworzyć odpowiedni konstruktor.
"""

# Koło
# r - promień; Pi - stała Pi, 3.14, math.pi
# Pole: Pi*r^2
# Obwód: 2*Pi*r

# Kwadrat
# a - długość boku kwadratu
# Pole: a*a
# Obwód: 4*a

# Konstruktor `__init__`

from math import pi

class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        pole = pi * self.promien ** 2
        return pole
    
    def oblicz_obwod(self):
        return 2 * pi * self.promien
    
# Test - Koło
k1 = Kolo(10)
k2 = Kolo(20)

print(k1.oblicz_obwod())
print(k1.oblicz_pole())

print(k2.oblicz_obwod())
print(k2.oblicz_pole())