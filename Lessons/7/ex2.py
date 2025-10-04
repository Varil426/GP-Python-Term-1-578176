"""
Napisz program odliczania dla bomby.
Program powinien wczytać od użytkownika liczbę całkowitą i odliczać od niej do zera,
wyświetlając na ekranie kolejne liczby.
Po zakończeniu odliczania powinien wyświetlić komunikat "BOOM!".
"""

import time

# 1. Pobrać od użytkownika liczbę całkowitą ✅
# 2. Odliczenie od podanej liczby do 0 ✅
# 3. Wyświetlenie "BOOM!" ✅

liczba = int(input("Podaj liczbę: "))

while liczba >= 0:
    time.sleep(1)
    print(liczba)
    liczba = liczba - 1

print("BOOM!")