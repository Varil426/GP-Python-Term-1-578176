"""
Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od użytkownika tyle komunikatów.
Na koniec wyświetli je w tej samej kolejności.

Dodatkowo: Spróbuj wyświetlić komunikaty w odwrotnej kolejności.
"""

# 1. Program pyta o liczbę elementów ✅
# 2. Program odczytuje podaną ilość komunikatów ✅
# 3. Program wyświetla je w tej samej kolejnośći ✅
# 4. DODATKOWE: Wyświetlenie w odwrotnej kolejności ✅

ilosc_komunikatow = int(input("Podaj ilość komunikatów: "))
tabela_komunikatow = []

for _ in range(ilosc_komunikatow):
    komunikat = input("Podaj komunikat: ")
    tabela_komunikatow.append(komunikat)

# Wyświetlamy je testowo w jednej linijce
print(tabela_komunikatow)

# Wyświetlanie w kolejności pierwotnej
for element in tabela_komunikatow:
    print(element)

# Wyświetlanie w kolejności odwrotnej
for przesuniecie in range(len(tabela_komunikatow)):
    index = len(tabela_komunikatow) - 1 - przesuniecie
    print(tabela_komunikatow[index])