def glowne_menu():
    print("Wybierz opcje:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")


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


# powyżej nich będziemy pisać wszystkie funkcje naszego programu!!!
wybor = 0
saldo = 0
# poniżej będzie główna pętla programu
while wybor != 4:
    glowne_menu()
    wybor = pobierz_wybor_klienta()
    if wybor == 1:
        saldo = wplata(saldo)
        pass
    elif wybor == 2:
        saldo = wyplata(saldo)
        pass
    elif wybor == 3:
        pokaz_stan_konta(saldo)
        pass
    elif wybor == 4:
        print("Wyłączanie bankomatu")
        pass
    else:
        print("niepoprawne dane")
        pass
    pass
