"""
Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych od Twojego roku urodzenia.
Program powinien wykorzystać zmienną wiek oraz pętle `for` z instrukcją `range`.
"""

wiek_rocznikowo = 26
obecny_rok = 2025

for i in range(wiek_rocznikowo + 1):
    wybrany_rok_kalendarzowy = obecny_rok - wiek_rocznikowo + i
    wiek_w_wybrany_roku_kalendarzowym = i

    print(f"W roku {wybrany_rok_kalendarzowy} miałeś/aś {wiek_w_wybrany_roku_kalendarzowym} lat")
