import random

kosci = [2, 1, 3, 6, 4]


nazwy_punktow = [
    "Jedynki",
    "Dwójki",
    "Trójki",
    "Czwórki",
    "Piątki",
    "Szóstki",
    "3 jednakowe",
    "4 jednakowe",
    "Full",
    "Mały strit",
    "Duży strit",
    "Generał",
    "Szansa",
]
punkty = ["", "", "", "", "", "", "", "", "", "", "", "", ""]


def rzuc_koscmi(numery_kosci: str):
    for i in numery_kosci:
        index = int(i) - 1
        kosci[index] = random.randint(1, 6)


def pokaz_kosci():
    print("_________________________")
    for i in range(len(kosci)):
        print(f"{i+1}. {kosci[i]}")
    print("_________________________")


def sprawdz_czy_przerzucamy():
    odp = input("czy chcesz przerzucać kości?(t/n) ")
    if odp == "t" or odp == "T":
        return True
    else:
        return False


def pokaz_tabele_punktow():
    print("_________________________")
    for i in range(len(punkty)):
        print(f"{i+1}.{nazwy_punktow[i]}\t{punkty[i]}")
    print("_________________________")


def wstaw_w_liczbowym(liczba):
    liczba_punktow = 0
    for kosc in kosci:
        if kosc == liczba:
            liczba_punktow += kosc
    punkty[liczba - 1] = liczba_punktow


def wstaw_3i4_jednakowe(pole, ilosc):
    lista_wystapien = [0, 0, 0, 0, 0, 0]
    for kosc in kosci:
        lista_wystapien[kosc - 1] += 1
    if ilosc in lista_wystapien:
        punkty[pole - 1] = sum(kosci)
    else:
        punkty[pole - 1] = 0


def wstaw_full(pole):
    lista_wystapien = [0, 0, 0, 0, 0, 0]
    for kosc in kosci:
        lista_wystapien[kosc - 1] += 1
    if 3 in lista_wystapien and 2 in lista_wystapien:
        punkty[pole - 1] = 25
    else:
        punkty[pole - 1] = 0


def wstaw_duzy_strit(pole):
    kosci.sort()
    dlugosc_strita = 0
    for i in range(1, 5):
        if kosci[i - 1] == kosci[i] - 1:
            dlugosc_strita += 1
        else:
            dlugosc_strita = 0
    if dlugosc_strita == 4:
        punkty[pole - 1] = 40
    else:
        punkty[pole - 1] = 0


def wstaw_maly_strit(pole):
    kosci_bez_powtorzen = list(set(kosci))
    kosci_bez_powtorzen.sort()
    dlugosc_strita = 0
    for i in range(len(kosci_bez_powtorzen) - 1, 0, -1):
        if kosci_bez_powtorzen[i] == kosci_bez_powtorzen[i - 1] + 1:
            dlugosc_strita += 1
            if dlugosc_strita == 3:
                punkty[pole - 1] = 30
                return
        else:
            dlugosc_strita = 0
    punkty[pole - 1] = 0


def wstaw_general(pole):
    lista_wystapien = [0, 0, 0, 0, 0, 0]
    for kosc in kosci:
        lista_wystapien[kosc - 1] += 1
    if 5 in lista_wystapien:
        punkty[pole - 1] = 50
    else:
        punkty[pole - 1] = 0


def wstaw_szansa(pole):
    punkty[pole - 1] = sum(kosci)


def wstaw_punkty():
    pole = int(input("Gdzie chcesz wstawić punkty (podaj numer rubryki): "))
    if punkty[pole - 1] == "":
        if 1 <= pole <= 6:
            wstaw_w_liczbowym(pole)
        elif pole == 7:
            wstaw_3i4_jednakowe(pole, 3)
        elif pole == 8:
            wstaw_3i4_jednakowe(pole, 4)
        elif pole == 9:
            wstaw_full(pole)
        elif pole == 10:
            wstaw_maly_strit(pole)
        elif pole == 11:
            wstaw_duzy_strit(pole)
        elif pole == 12:
            wstaw_general(pole)
        elif pole == 13:
            wstaw_szansa(pole)
    else:
        print("Wybrałeś pole w którym już wstawiłeś punkty")
        wstaw_punkty()


for tura in range(13):
    rzuc_koscmi("12345")
    pokaz_tabele_punktow()
    pokaz_kosci()
    for i in range(2):
        czy_przerzut = sprawdz_czy_przerzucamy()
        if czy_przerzut:
            kosci_do_przerzutu = input(
                "Wypisz numery kości, które chcesz przerzucić(bez spacji): "
            )
            rzuc_koscmi(kosci_do_przerzutu)
            pokaz_kosci()
        else:
            break
    pokaz_tabele_punktow()
    pokaz_kosci()
    wstaw_punkty()
    pokaz_tabele_punktow()

print(f"Twój wynik to: {sum(punkty)}")
