"""
Napisz funkcję, która otrzymuje liczbę całkowitą a zwraca sumę jej cyfr.

Przykład:
Dla liczby 249 otrzymujemy 2+4+9, czyli 15".
"""

def suma_cyfr(liczba: int) -> int:
    suma = 0
    liczba_tekst = str(liczba)
    for znak_cyfra in liczba_tekst:
        cyfra = int(znak_cyfra)
        suma += cyfra
    return suma

print(suma_cyfr(249))