"""
Wracając do naszego rollercoaser'a. Zarząd parku rozrywki mówi, że pojawiło się dodatkowe ogranicznie - wzrost maksymalny.
Aby możliwe było przejechanie się wagonikiem należy być wyższym niż minimalny wzrost,
ale jednocześnie być niższym niż wzrost maksymalny.

Kryterium:
Wzrost musi być większy niż 150 cm i wzrost musi być mniejszy niż 215 cm.

Rozwińmy nasze poprzednie rozwiązanie, aby uwzględniało oba kryteria.
"""

print("Czy możesz skorzystać z kolejki?")
print("True - tak, możesz skorzystać.")
print("False - nie, niestety nie możesz skorzystać.")

odp = input("Podaj swój wzrost [cm]: ")
odp_int = int(odp)

# werdykt = odp_int > 150 and odp_int < 215 # Zaktualizowana linijka
werdykt = 150 < odp_int < 215 # Comparison operator chaining
print(werdykt)
