"""
Uzupełnij wywołania funkcji range w taki sposób, aby uzyskać liczby podane w komentarzu.
Należy zastosować najkrótszą wersję wywołania, jeśli więcej niż jedna opcja jest możliwa.
"""

print("===========================")
# 0, 1, 2, 3, 4
for i in range(5):
    print(i)

print("===========================")
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i)

print("===========================")
# 5, 6, 7, 8, 9, 10, 11, 12
for i in range(5,13):
    print(i)

print("===========================")
# -5, -4, -3
for i in range(-5, -2):
    print(i)

print("===========================")
# 2, 4, 6, 8, 10
for i in range(2, 12, 2):
    print(i)

print("===========================")
# 0, 5, 10, 15
for i in range(0, 20, 5):
    print(i)

print("===========================")
# -9 -6 -3 0 3
for i in range(-9, 6, 3):
    print(i)

print("===========================")
# -100 -25 50 125
for i in range(-100, 125, 75):
    print(i)