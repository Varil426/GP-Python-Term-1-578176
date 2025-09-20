"""
Stwórzmy program obliczający wynik z dzielenia.
Pamiętaj, że nie wolno dzielić przez zero.
"""

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

if dzielnik == 0:
    print("Nie wolno dzielić przez 0")

if dzielnik != 0:
    wynik = dzielna / dzielnik
    print(f"Wynik dzielenia {dzielna} przez {dzielnik} wynosi {wynik}")