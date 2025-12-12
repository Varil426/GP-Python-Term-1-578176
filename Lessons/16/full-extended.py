def glowne_menu():
    print("Wybierz opcje:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")
    print("5. Wyświetlenie histori operacji")


def pobierz_wybor_klienta():
    return int(input("twój wybór to: "))


def pobierz_kwote(tekst):
    return float(input(tekst))


def pokaz_stan_konta(saldo):
    print(f"Stan konta wynosi {saldo} złotych")


def wplata(saldo):
    kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić")
    saldo = saldo + kwota_wplaty
    pokaz_stan_konta(saldo)
    return saldo


def wyplata(saldo):
    kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić")
    if kwota_wyplaty > saldo:
        print("Operacja nie udana, za mało środków na koncie")
        return saldo
    else:
        saldo -= kwota_wyplaty
        print(f"Wypłacono {kwota_wyplaty} złotych")
        return saldo


def pobierz_dane(dana):
    return input(f"Podaj numer {dana}: ")


def sprawdz_zgodnosc_danych(baza, karta, pin):
    for klient in baza:
        if klient[0] == karta:
            return klient[1] == pin
    return False


def pobierz_stan_konta(baza, karta):
    for klient in baza:
        if klient[0] == karta:
            return klient[2]
    return 0


def aktualizuj_historie_klienta(baza, karta, operacja):
    for klient in baza:
        if klient[0] == karta:
            klient[3].append(operacja)


def pokaz_historie_klienta(baza, karta):
    for klient in baza:
        if klient[0] == podana_karta:
            for i in range(len(klient[3])):
                print(f"{i+1}. {klient[3][i]}")


# powyżej nich będziemy pisać wszystkie funkcje naszego programu!!!
wybor = 0
saldo = 0
# KARTA = "0001"
# PIN = "1234"
KLIENCI = [
    ["0001", "1234", 0, []],
    ["0002", "1111", 120, []],
    ["0003", "3232", 1223.33, []],
]
# poniżej będzie główna pętla programu
podana_karta = pobierz_dane("karty")
podany_pin = pobierz_dane("PIN")
if sprawdz_zgodnosc_danych(KLIENCI, podana_karta, podany_pin):
    saldo = pobierz_stan_konta(KLIENCI, podana_karta)
    while wybor != 4:
        glowne_menu()
        wybor = pobierz_wybor_klienta()
        if wybor == 1:
            saldo = wplata(saldo)
            aktualizuj_historie_klienta(KLIENCI, podana_karta, "Wpłata")
            pass
        elif wybor == 2:
            saldo = wyplata(saldo)
            aktualizuj_historie_klienta(KLIENCI, podana_karta, "Wypłata")
            pass
        elif wybor == 3:
            pokaz_stan_konta(saldo)
            aktualizuj_historie_klienta(KLIENCI, podana_karta, "Wyświetlenie salda")
            pass
        elif wybor == 4:
            print("Wyłączanie bankomatu")
            pass
        elif wybor == 5:
            pokaz_historie_klienta(KLIENCI, podana_karta)
            pass
        else:
            print("niepoprawne dane")
            pass
        pass
else:
    print("błąd logowania")
