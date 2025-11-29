"""
Napisz program, który zapyta użytkownika o liczbę,
a następnie wypisze na ekranie tyle wyników z rzutu kością sześcienną.

Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).
"""
import random

def rzut():
    MIN = 1
    MAX = 6
    wynik = random.randint(MIN, MAX)
    return wynik

ilosc_rzutow = int(input("Podaj ilość rzutów: "))

for _ in range(ilosc_rzutow):
    print(rzut())