"""
Cena atrakcji turystycznej zależy od miesiąca.
Napisz program, który zapyta użytkownika o liczbę biletów oraz miesiąc,
w którym chce odwiedzić park rozrywki i na tej podstawie obliczy koszt transakcji.

Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł
- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł

Wyświetl komunikat:
"Cena biletów: XX zł"

"XX" to wartość liczbowa.

Jeśli wprowadzono niepoprawny numer miesiąca program powinien wyświetlić informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"
"""

liczba_biletow = int(input("Podaj liczbę biletów: "))
miesiac = int(input("Podaj miesiąc: "))

cena_biletu = 250

if miesiac == 1 or miesiac == 2 or miesiac == 12:
    cena_biletu = 50
elif miesiac == 3 or miesiac == 4 or miesiac == 10 or miesiac == 11:
    cena_biletu = 100
elif miesiac == 5 or miesiac == 6 or miesiac == 8 or miesiac == 9:
    cena_biletu = 200
elif miesiac == 7:
    # cena_biletu = 250
    pass
else:
    print("Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie")
    exit()

cena = cena_biletu * liczba_biletow
print(f"Cena biletów: {cena} zł")