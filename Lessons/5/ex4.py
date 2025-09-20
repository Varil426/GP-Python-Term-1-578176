"""
Stwórz program, który poprosi użytkownika o podanie liczby, a następnie określi jej znak.
Jaką liczbę całkowitą wprowadzono: pozytywną, negatywną, czy równą zero?
"""

liczba = int(input("Podaj liczbę: "))

if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0:
    print("Liczba jest ujemna")
# elif liczba == 0:
else:
    print("Liczba jest równa zero")