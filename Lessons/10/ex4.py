"""
Napisz funkcję, która przyjmuje dwa argumenty: `n` - liczba powtórzeń, `a` - liczba startowa.
Funkcja ma generować kolejne kwadraty liczb, zaczynając od `a` i ma wyświetlić `n` kolejnych liczb.

Dodatkowo: Wartość domyślna dla `n` to 10.
"""

def kwadraty_liczb(a, n = 10):
    for i in range(n):
        liczba = a + i
        wynik = liczba ** 2
        print(f"Liczba {liczba} do kwadratu to {wynik}")

kwadraty_liczb(2, 5)

kwadraty_liczb(2)