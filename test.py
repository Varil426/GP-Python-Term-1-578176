# a = input("Podaj liczbę: ")

# a1 = "123"
# a2 = 123

# w1 = a1 + "5"
# w2 = a2 + 5

# print(w1) # 1235
# print(w2) # 128

# w2 = 101

# if w2 > 100:
#     print("TEST 1")
#     print("TEST 2")




#     print("TEST 3")
# else:
#     print("TEST 4")

# for
# print("for:\n")
# for i in range(10, 0, -1):
#     print("TEST")

# # while
# print("while:\n")
# i = 10
# while i > 0:
#     print("TEST")
#     i -= 1

# moja_lista = []
# moja_lista = [7, 4, 2]

# print(moja_lista[-2])

# print(moja_lista)
# moja_lista.append(3)
# print(moja_lista)

# def dodaj(a: int, b: int) -> int:
#     wynik = a + b
#     return wynik

# test = 123
# print(dodaj(dodaj(5, 6), 2))


zmienna_sterujca = 0
while True:
    print("TEST")

    zmienna_sterujca += 1

    if zmienna_sterujca == 30:
        break


for i in range(50):
    if i % 7 != 0:
        continue

    print(i)