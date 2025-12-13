wybor = 0
saldo = 0

def glowne_menu():
    print("Wybierz opcje:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")

def pobierz_wybor_klienta():
    return int(input("Twój wybór: "))

def pokaz_stan_konta(saldo):
    print(f"Stan konta wynosi {saldo} złotych")

def pobierz_kwote(komunikat):
    return float(input(komunikat))

def wplata(saldo):
    kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić? ")
    saldo = saldo + kwota_wplaty
    pokaz_stan_konta(saldo)
    return saldo

def wyplata(saldo):
    kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić? ")
    if kwota_wyplaty > saldo:
        print("Operacja nieudana. Za mało środków na koncie.")
        return saldo
    else:
        saldo -= kwota_wyplaty
        print(f"Wypłacono {kwota_wyplaty} złotych")
        pokaz_stan_konta(saldo)
        return saldo

while wybor != 4:
    glowne_menu()
    wybor = pobierz_wybor_klienta()

    if wybor == 1:
        saldo = wplata(saldo)
    elif wybor == 2:
        saldo = wyplata(saldo)
    elif wybor == 3:
        pokaz_stan_konta(saldo)
    elif wybor == 4:
        pass
    else:
        print("Nieprawidłowa opcja")

print("Wyłączanie systemu!")