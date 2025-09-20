"""
Park rozrywki wprowadza kolejne ograniczenia dotyczące korzystania z nowej atrakcji.

Napisz program, który powie Ci czy dany uczestnik może skorzystać z nowej atrakcji.

Ograniczenia:
- minimalny akceptowalny wiek to 12 lat,
- minimalny akceptowalny wzrost to 130 cm,
- maksymalny akceptowalny wzrost to 195 cm.

Program powinien zapytać użytkownika o jego wiek i wzrost,
a następnie wyświetli komunikat, czy wolno mu skorzystać z atrakcji.
"""

wiek = int(input("Podaj ile masz lat: "))
wzrost = int(input("Podaj swój wzrost [cm]: "))

if wiek >= 12 and wzrost >= 130 and wzrost <= 195:
    print("Wolno Ci skorzystać z atrakcji")
else:
    print("Nie wolno Ci skorzystać z atrakcji")