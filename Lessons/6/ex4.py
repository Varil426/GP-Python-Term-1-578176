"""
Napisz program, który wczyta od użytkownika długości trzech boków trójkąta, a następnie:
1. Sprawdzi, czy podany trójkąt może istnieć.
2. Wyświetli:
  - najkrótszy bok trójkąta,
  - najdłuższy bok trójkąta,
  - rodzaj trójkąta (równoboczny, równoramienny, różnoboczny),
  - obwód trójkąta,
  - rodzaj trójkąta względem kątów (ostrokątny, prostokątny, rozwartokątny).

Najpierw zastanów się, jakie warunki muszą być spełnione, aby:
- trójkąt mógł istnieć,
- trójkąt był równoboczny, równoramienny lub różnoboczny,
- trójkąt był ostrokątny, prostokątny lub rozwartokątny.
"""

bok1 = float(input("Podaj długość pierwszego boku: "))
bok2 = float(input("Podaj długość drugiego boku: "))
bok3 = float(input("Podaj długość trzeciego boku: "))

print(f"Podano boki: {bok1}, {bok2}, {bok3}")

najkrotszy = min(bok1, bok2, bok3)
najdluszy = max(bok1, bok2, bok3)
obwod = bok1 + bok2 + bok3

# Sprawdzenie danych
if bok1 <= 0 or bok2 <= 0 or bok3 <= 0:
    print("Niepoprawne dane")
    exit()

# Czy można utworzyć trójkąt
if not (bok1 + bok2 > bok3 and bok2 + bok3 > bok1 and bok1 + bok3 > bok2):
    print("Nie można utworzyć trójkąta z podanych boków")
    exit()

# Wypisanie najdłuższego i najkrótszego boku
print(f"Najkrótszy bok: {najkrotszy}")
print(f"Najdłuższy bok: {najdluszy}")

# Rodzaj trójkąta ze względu na boki
if bok1 == bok2 == bok3:
    print("Trójkąt równoboczny")
elif bok1 != bok2 and bok1 != bok3 and bok2 != bok3:
    print("Trójkąt różnoboczny")
else:
    print("Trójkąt równoramienny")

# Wypisanie obwodu
print(f"Obwód: {obwod}")

# Rodzaj trójkąta ze względu na kąty
# Twierdzenie pitagorasa
sredni_bok = obwod - najdluszy - najkrotszy
pitagoras = najkrotszy ** 2 + sredni_bok ** 2

# pitagoras == najdluszy ** 2 - prosokątny
# pitagoras < najdluszy ** 2 - rozwartokątny
# pitagoras > najdluszy ** 2 - ostrokątny