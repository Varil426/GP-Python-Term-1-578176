"""
Zgadywanie liczby wylosowanej przez komputer.
Program losuje liczbę, a zadaniem użytkownika jest odgadnąć ją.
Komputer odpowiada "za mało", "za dużo", a w przypadku trafienia wyświetla informację o
wygranej i liczbie tur potrzebnych do wygranej.
"""

import random

MINIMUM = 1
MAXIMUM = 1000000

wylosowana_liczba = random.randint(MINIMUM, MAXIMUM)

# Dla testów
print(wylosowana_liczba)

odpowiedz = None
licznik_tur = 0

while odpowiedz != wylosowana_liczba:
    odpowiedz = int(input("Podaj liczbę: "))
    licznik_tur += 1

    if odpowiedz < wylosowana_liczba:
        print("Za mało")
    elif odpowiedz > wylosowana_liczba:
        print("Za dużo")

print(f"Gratulacje! Udało Ci się odgadnąć wylosowaną liczbę w {licznik_tur} turach")
