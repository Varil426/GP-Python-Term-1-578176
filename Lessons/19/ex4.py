"""
Napisz program, który zliczy ilość słów i wytąpień poszczególnych liter w podanym przez użytkownika tekście.

Przykładowe wyświetlanie:

ABC przykladowy tekst na potrzeby naszego programu

Slowa: 7 Litery: 44 ilosc liter:
{
    "a": 5,
    "b": 2,
    "c": 1,
    "p": 3,
    "r": 4,
    "z": 3,
    "y": 3,
    "k": 2,
    "l": 1,
    "d": 1,
    "o": 4,
    "w": 1,
    "t": 3,
    "e": 3,
    "s": 2,
    "n": 2,
    "g": 2,
    "m": 1,
    "u": 1,
}

"""

tekst = "ABC przykladowy tekst na potrzeby            naszego programu "
print(f"Tekst: {tekst}")

slowa  = 0
if len(tekst.strip()) > 0:
    slowa += 1

litery = 0
wystapienia = {}

czy_ostatnia_spacja = False
for znak in tekst.strip().lower():
    if znak == ' ':
        if not czy_ostatnia_spacja:
            slowa += 1
            czy_ostatnia_spacja = True
    else:
        czy_ostatnia_spacja = False
        litery += 1
        if znak in wystapienia:
            wystapienia[znak] += 1
        else:
            wystapienia[znak] = 1


print(f"Słowa: {slowa}, Litery: {litery}, Ilość liter: {wystapienia}")