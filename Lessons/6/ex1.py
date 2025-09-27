"""
Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie
znajduje się jedna z następujących liter lub ciągów znaków:
- litera "a"
- litera "d"
- ciąg znaków "as"
- ciąg znaków "zzz"

Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat,
że wyraz zawiera poszukiwany fragment.
"""

# 1. Pobrać wyraz - input()
# 2. Sprawdzić warunek - if, in, and
# 3. Wypisać odpowiedni komunikat

tekst_od_uzytkownika = input("Podaj tekst: ")

if "a" in tekst_od_uzytkownika or "d" in tekst_od_uzytkownika or "as" in tekst_od_uzytkownika or "zzz" in tekst_od_uzytkownika:
    print("Przynajmniej jeden z poszukiwanych fragmentów znajduje się w tekście.")
else:
    print("Żaden z poszukiwanych fragmentów nie znajduje się w tekście.")