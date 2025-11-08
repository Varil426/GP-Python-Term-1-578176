"""
Napisz funkcję, która przyjmuje następujące argumenty:
- imie (str),
- wiek (int),
- wzrost_m (float),
a zwraca napis:
"Jan, lat 20, 1.75 m wzrostu" - oczywiście argumenty należy podstawić do szablonu.
Wzrost ma zawsze pokazywać dwa miejsca po przecinku.
"""

def info(imie: str, wiek: int, wzrost_m: float) -> str:
    return f"{imie}, lat {wiek}, {wzrost_m:.2f} m wzrostu"

print(info("Bartek", 26, 1.822412312313))
