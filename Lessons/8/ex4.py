"""
Napisz program, który wypisze w konsoli tabliczkę mnożenia.
Wykorzystaj funkcję `str(liczba).center(liczba_znaków)` do wyrównania tekstu.
"""

for a in range(1, 11):
    linijka  = "|"
    for b in range(1, 11):
        obecna_liczba = a * b
        linijka += f"{str(obecna_liczba).center(5)}|"
    print(linijka)
    print("-" * len(linijka))