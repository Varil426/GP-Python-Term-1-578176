"""
Napisz program, który z listy pokaże nam najmniejszą i największą liczbę.
"""

lista = [1,3,7,11,2,-6,0]

min = lista[0]
max = lista[0]

for element in lista:
    # min
    if element < min:
        min = element

    # max
    if element > max:
        max = element

print(f"Min to {min}")
print(f"Max to {max}")
