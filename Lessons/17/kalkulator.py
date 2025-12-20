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

def przetlumacz(slowo):
    for baza_symbolu in baza:
        for slowo_bazy_symbolu in baza_symbolu:
            if slowo == slowo_bazy_symbolu:
                return baza_symbolu[0]
    return ''

def oblicz_z_tekstu(tekst):
    wynik = 0
    liczba = ''
    operacja = ''

    for znak in tekst:
        if znak.isdigit():
            liczba += znak
        # else:
        elif liczba:
            if operacja == '':
                wynik = int(liczba)
            else:
                wynik = oblicz(wynik, int(liczba), operacja)
            liczba = ''
            operacja = znak
    if liczba:
        wynik = oblicz(wynik, int(liczba), operacja)
    return wynik

def oblicz(liczba1, liczba2, operacja):
    if operacja == "+":
        return liczba1 + liczba2
    elif operacja == "-":
        return liczba1 - liczba2
    elif operacja == "*":
        return liczba1 * liczba2
    elif operacja == "/":
        return liczba1 / liczba2

dzialanie = ""
tekst = input("Podaj tekst: ")

for slowo in tekst.split(" "):
    dzialanie += przetlumacz(slowo)

print(f"Otrzymane działanie: {dzialanie}")
print(f"Wynik: {oblicz_z_tekstu(dzialanie)}")