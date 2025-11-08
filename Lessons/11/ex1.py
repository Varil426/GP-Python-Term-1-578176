"""
Przygotuj funkcję, która jako argument otrzymuje string oraz listę stringów, a zwraca napis,
gdzie pomiędzy elementy z listy dokładana jest zawartość pierwszego argumentu.

Wskazówka: skorzystaj z metody `join`

Przykład:
foo("?", ["ala", "ma", "kota"]) -> "ala?ma?kota"
"""

def foo(fraza, lista_wyrazow):
    wynik = fraza.join(lista_wyrazow)
    return wynik

print(foo("GP", ["bartek", "kamil", "janusz"]))

# Wersja manualna
def foo_2(fraza, lista_wyrazow):
    nowy_wyraz = lista_wyrazow[0]
    for wyraz in lista_wyrazow[1:]:
        nowy_wyraz += fraza
        nowy_wyraz += wyraz
    return nowy_wyraz

print(foo_2("GP", ["bartek", "kamil", "janusz"]))
