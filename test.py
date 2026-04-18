# listę o długości 20, z losowymi elementami z zakresu 1-100

import random

lista = []

for _ in range(20):
    lista.append(random.randint(1, 100))

print(lista)