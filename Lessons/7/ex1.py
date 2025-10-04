"""
Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli na ekranie
dokładnie tyle komunikatów "Giganci Programowania".
"""

ilosc_komunikatow = int(input("Podaj ilość: "))

licznik = 0
while licznik < ilosc_komunikatow:
    print("Giganci Programowania")
    licznik += 1