"""
Utwórz 3 zmienne:
- `pole_trojkata`,
- `podstawa_trojkata`,
- `wysokosc_trojkata`.

Do `podstawa_trojkata` oraz `wysokosc_trojkata` powinny trafić wartości odczytane z konsoli (od użytkownika).
Oblicz pole takiego trójkąta i zapisz wynik w zmiennej `pole_trojkata`.

Wyświetl wynik jako komunikat:
"Pole trójkąta o podstawie XX oraz wysokości XX wynosi XX"
Zamiast "XX" powinny pojawić się wartości liczbowe.
"""

podstawa_trojkata = float(input("Jaka jest podstawa trójkąta? "))
wysokosc_trojkata = float(input("Jaka jest wysokość trójkąta? "))

pole_trojkata = podstawa_trojkata * wysokosc_trojkata / 2

print(f"Pole trójkąta o podstawie {podstawa_trojkata} oraz wysokości {wysokosc_trojkata} wynosi {pole_trojkata}")