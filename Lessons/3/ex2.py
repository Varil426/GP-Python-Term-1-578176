"""
Napisz program, który zapyta i pobierze od użytkownika dwie liczby,
a następnie wypisze na konsoli wynik tego działania, podając całości i resztę z dzielenia.

Przykład: Dla danych 48 i 10: "48 dzielone przez 10 jest równe 4 i 8 reszty."
"""

# // - dzielenie całkowite
# % - reszta z dzielenia

dzielna = int(input("Podaj dzielną: "))
dzielnik = int(input("Podaj dzielnik: "))

print(f"{dzielna} dzielone przez {dzielnik} jest równe {dzielna // dzielnik} i {dzielna % dzielnik} reszty.")