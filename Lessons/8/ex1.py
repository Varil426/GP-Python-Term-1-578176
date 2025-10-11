"""
Napisz program, który będzie pytać użytkownika o liczby i zliczać ich sumę, aż do wprowadzenia przez użytkownika hasła "koniec".
Po wpisaniu tego hasła program, powinien opuścić pętle while i wyświetlić sumę tych liczb.
"""

suma = 0

while True:
    user_input = input("Podaj liczbę lub 'koniec': ")

    if user_input == 'koniec':
        break
    
    liczba = int(user_input)
    # suma = suma + liczba
    suma += liczba

print(f"Suma = {suma}")