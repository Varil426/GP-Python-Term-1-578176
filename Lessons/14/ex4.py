"""
Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z komunikatów:
- "Jesteś pełnoletni/a".
- "Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia".
Zamiast "XX" powinna pojawić się wartość liczbowa.
"""

wiek_str = input("Ile masz lat? ")
wiek_int = int(wiek_str)

if wiek_int < 18:
    roznica = 18 - wiek_int
    print(f"Nie jesteś jeszcze pełnoletni/a. Brakuje Ci {roznica} lat do 18 roku życia")
else:
    print("Jesteś pełnoletni/a")