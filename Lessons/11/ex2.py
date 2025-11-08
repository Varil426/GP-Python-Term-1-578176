"""
Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba,
którą chcemy podzielić bez reszty a drugim argumentem będzie dzielnik.
Należy sprawdzić czy można dokonać dzielenia, a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.
"""

def podzielna(liczba, dzielnik):
    if dzielnik == 0:
        return "Nie można dzielić przez 0"
    
    reszta_z_dzielenia = liczba % dzielnik
    if reszta_z_dzielenia == 0:
        return f"Liczba {liczba} jest podzielna przez {dzielnik} bez reszty"
    else:
        return f"Liczba {liczba} nie jest podzielna przez {dzielnik} bez reszty. Reszta wynosi {reszta_z_dzielenia}"
    
print(podzielna(6,5))
print(podzielna(1024,2))