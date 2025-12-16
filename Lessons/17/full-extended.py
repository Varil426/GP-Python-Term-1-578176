zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jedynkę"]
dwa = ["2", "dwa", "dwójkę", "dwójka"]
trzy = ["3", "trzy", "trójkę", "trójka"]
cztery = ["4", "cztery", "czwórkę", "czwórka"]
piec = ["5", "pięć", "piątkę", "piątka"]
szesc = ["6", "sześć", "szóstkę", "szóstka"]
siedem = ["7", "siedem", "siódemkę", "siódemka"]
osiem = ["8", "osiem", "ósemkę", "ósemka"]
dziewiec = ["9", "dziewięć", "dziewiątkę", "dziewiątka"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątkę", "dychę"]
jedenascie = ["11", "jedenaście", "jedenastkę", "jedenastu"]
dwanascie = ["12", "dwanaście", "dwunastu", "dwunastkę"]
trzynascie = ["13", "trzynaście", "trzynastu", "trzynastkę"]
czternascie = ["14", "czternaście", "czternastu", "czternastkę"]
pietnascie = ["15", "piętnaście", "piętnastu", "piętnastkę"]
szesnascie = ["16", "szesnaście", "szesnastu", "szesnastkę"]
siedemnascie = ["17", "siedemnaście", "siedemnastu", "siedemnastkę"]
osiemnasice = ["18", "osiemnaście", "osiemnastu", "osiemnastkę"]
dziewietnascie = ["19", "dziewiętnaście", "dziewiętnastu", "dziewiętnastkę"]
plus = ["+", "dodaj", "plus", "dodać"]
minus = ["-", "odejmij", "minus", "odjąć"]
gwiazdka = ["*", "x", "razy", "mnożone", "pomnożone", "pomnożyć"]
ukosnik = ["/", ":", "dzielone", "podziel"]
baza = [
    zero,
    jeden,
    dwa,
    trzy,
    cztery,
    piec,
    szesc,
    siedem,
    osiem,
    dziewiec,
    dziesiec,
    jedenascie,
    dwanascie,
    trzynascie,
    czternascie,
    pietnascie,
    szesnascie,
    siedemnascie,
    osiemnasice,
    dziewietnascie,
    plus,
    minus,
    gwiazdka,
    ukosnik,
]
dziesiatki = ["dzieścia", "dziesiąt", "dzieści"]

byla_dziesiatka = -1


def przetlumacz(slowo):
    global byla_dziesiatka
    for koncowka in dziesiatki:
        if slowo.endswith(koncowka):
            byla_dziesiatka = 1
            slowo = slowo.replace(koncowka, "")

    for baza_symbolu in baza:
        for slowo_bazy_symbolu in baza_symbolu:
            if slowo == slowo_bazy_symbolu:
                if byla_dziesiatka == 0 and not baza_symbolu[0].isdigit():
                    byla_dziesiatka = -1
                    return "0" + baza_symbolu[0]
                else:
                    byla_dziesiatka -= 1
                    return baza_symbolu[0]
    return ""  # jeśli słowo które próbujemy przetłumaczyć na liczbę lub operator nie występuje w naszych tablicach to je pomijamy


def oblicz(liczba1, liczba2, operacja):
    if operacja == "+":
        return liczba1 + liczba2
    elif operacja == "-":
        return liczba1 - liczba2
    elif operacja == "*":
        return liczba1 * liczba2
    elif operacja == "/":
        return liczba1 / liczba2


def oblicz_z_tekstu(tekst):
    wynik = 0
    liczba = ""
    operacja = ""
    for znak in tekst:
        if znak.isdigit():
            liczba += znak
        elif liczba:
            if operacja == "":
                wynik = int(liczba)
            else:
                wynik = oblicz(wynik, int(liczba), operacja)
            liczba = ""
            operacja = znak

    if liczba:
        wynik = oblicz(wynik, int(liczba), operacja)
    return wynik


kontynuowanie = ""
while kontynuowanie != "n":
    dzialanie = ""
    tekst = input("podaj tekst: ").lower()
    for slowo in tekst.split(" "):
        dzialanie += przetlumacz(slowo)
    if byla_dziesiatka == 0:
        dzialanie += "0"
    print(dzialanie)
    print(oblicz_z_tekstu(dzialanie))
    kontynuowanie = input("Czy chcesz kontynuować działanie programu (t/n)").lower()
print("Koniec")
