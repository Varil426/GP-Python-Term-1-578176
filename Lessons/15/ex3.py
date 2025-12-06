"""
Napisz funkcję, która zwróci informacje `True`/`False` czy podana liczba jest liczbą pierwszą.
"""


def czy_liczba_jest_pierwsza(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


# Testy
if __name__ == "__main__":
    print(czy_liczba_jest_pierwsza(7))  # powinno wyświetlić True
    print(czy_liczba_jest_pierwsza(11))  # powinno wyświetlić True
    print(czy_liczba_jest_pierwsza(4))  # powinno wyświetlić False
    print(czy_liczba_jest_pierwsza(1))  # powinno wyświetlić False
    print(czy_liczba_jest_pierwsza(2))  # powinno wyświetlić True

