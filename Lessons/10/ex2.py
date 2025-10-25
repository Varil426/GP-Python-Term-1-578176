"""
Przygotuj funkcję obliczającą pole prostokąta.
Funkcja ma przyjmować długości boków, a następnie obliczać i wyświetlać pole figury.

Dodatkowo: Funckję obliczająco pole trójkąta prostokątnego.
"""

def pole_prostokata(bok_1, bok_2):
    pole = bok_1 * bok_2
    print(f"Pole prostokąta o bokach {bok_1}, {bok_2} wynosi {pole}")

pole_prostokata(7, 6)
pole_prostokata(10, 10)
pole_prostokata(1, 3)