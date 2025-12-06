"""
Napisz funkcję, która jako argument otrzymuje tekst i sprawdzi czy jest on palindromem wyświetlając:
"{podane słowo} jest palindromem" lub "{podane słowo} nie jest palindromem".

Wersja rozszerzona: funkcja powinna ignorować wielkość liter oraz spacje.
"""


def czy_palindrom(text):
    odwrocony = text[::-1]
    if text == odwrocony:
        print(f"{text} jest palindromem")
    else:
        print(f"{text} nie jest palindromem")


# Testy
if __name__ == "__main__":
    czy_palindrom("kajak")  # powinno wyświetlić: kajak jest palindromem
    czy_palindrom("python")  # powinno wyświetlić: python nie jest palindromem
    czy_palindrom("ala")  # powinno wyświetlić: ala jest palindromem
