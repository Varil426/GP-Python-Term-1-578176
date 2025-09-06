"""
Procenty.
Pobierz od użytkownika liczbę, a następnie wartość procentową.
Program ma za zadanie wyświetlić ile to jest (% z liczby).
"""

liczba_z_ktorej_liczymy_procent = 64

podana_wartosc = int(input("Podaj liczbę: "))

wynik = podana_wartosc / liczba_z_ktorej_liczymy_procent * 100

print(f"{podana_wartosc} to jest {wynik}% z liczby {liczba_z_ktorej_liczymy_procent}")