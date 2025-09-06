"""
Pobierz od użytkownika imię, nazwisko, rok urodzenia i wypisz na konsolę informację (dla danych Jan Kowalski, 1996):
"Jan Kowalski ma rocznikowo 25 lat."
"""

imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")

rok_urodzenia = input("Podaj swój rok urodzenia: ")
rok_urodzenia_int = int(rok_urodzenia)

wiek = 2025 - rok_urodzenia_int

print(f"{imie} {nazwisko} ma rocznikowo {wiek} lat.")