"""
Napisz program, który będzie działał jak podstawowy system logowania.
Zacznij od ustalenia listy kroków, które należy wykonać, aby użytkownik mógł się zalogować.
"""

# 0. Przygotuj dane użytkownika - "stwórz konto"
# 1. Zapytaj użytkownika o login
# 2. Zapytaj użytkownika o hasło
# 3. Sprawdź czy dane są poprawne
# 3a. Dane poprawne - wyświetl komunikat o poprawny zalogowaniu
# 3b. Dane niepoprawne - wyświetl komunikat o błędzie

LOGIN = "gigant@trener.pl"
HASLO = "qwerty"

user_login = input("Login: ")
user_haslo = input("Hasło: ")

if user_login == LOGIN and user_haslo == HASLO:
    print("Poprawnie zalogowano na konto")
else:
    print("Błąd logowania - niepoprawne dane")