"""
Skoro wiemy, z jakimi problemami borykają się operatorzy rollercoaster'ów,
spróbujmy zaimplementować program, który ułatwi im podejmowanie decyzji.

Specyfikacja:
Program pytający użytkownika o jego wzrost, aby na tej podstawie określić czy może skorzystać z rollercoastera.

Kryterium:
Wzrost osoby, wyrażony w centymetrach, musi być większy niż 150.

Przed rozwiązaniem zadania, zastanów się:
- W jaki sposób sformułujemy zdanie opisujące werdykt pozytywny?
- Jaki musi być wzrost, aby wynik był prawdą?
"""

print("Czy możesz skorzystać z kolejki?")
print("True - tak, możesz skorzystać.")
print("False - nie, niestety nie możesz skorzystać.")

odp = input("Podaj swój wzrost [cm]: ")
odp_int = int(odp)

werdykt = odp_int > 150
print(werdykt)