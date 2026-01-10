from Uzytkownik import Uzytkownik

user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()

user1.imie = "Jan"
user1.nazwisko = "Kowalski"
user1.wiek = 32

user2.imie = "Adam"
user2.nazwisko = "Nowak"
user2.wiek = 12

user3.imie = "Piotr"
user3.nazwisko = "Murarz"
user3.wiek = 19

user1.wyswietl()
user2.wyswietl()
user3.wyswietl()

print("TEST Zadanie 1")
user1.wyswietl()
user1.zmien_wiek(15)
user1.wyswietl()

user1.zmien_wiek(-10)
user1.wyswietl()