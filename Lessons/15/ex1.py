"""
Napisz funkcję, która otrzyma jeden argument określający liczbę dziesiętną.
Funkcja ma wyświetlić ile wynosi podana liczba w zapisie binarnym.
"""


def binary(a: int):
    wynik = ''
    while(a>0):
        cyfra = a % 2
        a = a // 2
        wynik = str(cyfra) + wynik
    return wynik

# Testy
if __name__ == "__main__":
    print(binary(10))  # powinno wyświetlić 1010
    print(binary(4))  # powinno wyświetlić 100
