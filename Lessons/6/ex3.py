"""
Stwórz program, który obsłuży proces dwuetapowego logowania.
Użytkownik zostanie poproszony o wprowadzenie czterocyfrowego PIN'u.
Jeśli poda błędny PIN, program wyświetli odpowiedni komunikat o błędzie.
W przypadku poprawnego PIN'u, użytkownik zostanie następnie poproszony o podanie hasła słownego.

Poprawne dane do logowania to:
PIN: "1234"
Hasło: "Masło"

Zastanów się, czy PIN powinien być przechowywany jako tekst, czy liczba?
"""

PIN = "1234"
# LOGIN = "gigant@trener.pl"
HASLO = "Masło"

# user_login = input("Login: ")
user_pin = input("PIN: ")

if PIN == user_pin:
    user_haslo = input("Hasło: ")
    if HASLO == user_haslo:
        print("Poprawnie zalogowano")
    else:
        print("Błąd logowania - niepoprawne dane")
else:
    print("Błąd logowania - niepoprawne dane")