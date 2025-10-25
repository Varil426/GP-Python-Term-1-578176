"""
Napisz funkcję, który obliczy pole koła.
Skorzystaj w tym celu z modułu `math`, który zawiera stałą `pi`.
"""

import math

# Pole Koła = PI * r ^ 2

def pole_kola(r):
    # pole = math.pi * r * r
    # pole = math.pi * r ** 2
    pole = math.pi * math.pow(r, 2)
    print(f"Pole koła o promieniu {r} wynosi {pole}")

pole_kola(3)
pole_kola(10)