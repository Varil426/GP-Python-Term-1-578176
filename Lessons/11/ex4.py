"""
Napisz funkcję, która jako argument otrzymuje listę elementów,
w której mogą występować powtórzenia, a zwraca listę unikalnych elementów.

Przykład:
Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5].
"""

def filtruj(liczby: list[int]) -> list[int]:
    wynik = []
    for liczba in liczby:
        if liczba not in wynik:
            wynik.append(liczba)
    return wynik

print(filtruj([213,213,3,2,5,7,3]))