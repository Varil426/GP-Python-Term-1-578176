"""
Napisz funkcję, która otrzyma jeden argument określający liczbę binarną.
Funkcja ma wyświetlić ile wynosi podana liczba w zapisie dziesiętnym.
"""


def decimal(a):
    dec = 0
    i = 0
    while(a>0):
        mod = a % 10
        a //= 10 # a = a // 10
        dec += mod * 2**i
        i += 1
    return dec


# Testy
if __name__ == "__main__":
    print(decimal(101001))  # powinno wyświetlić 41
    print(decimal(111))  # powinno wyświetlić 7
