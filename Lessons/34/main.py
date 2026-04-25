import json
import os
from pprint import pprint

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("l1.json", "r") as file:
    spis_gier = json.load(file)

print("Wczytany JSON:")
pprint(spis_gier)

gra = {
    "tytul": "Counter-Strike 2",
    "rok_wydania": 2023,
    "wydawca": "Valve Corporation",
    "gatunek": "shooter, esport, competetive"
}

spis_gier["spis_gier"].append(gra)

print("Po dodaniu:")
pprint(spis_gier)

gry_po_2013 = []
for gra in spis_gier["spis_gier"]:
    if int(gra["rok_wydania"]) >= 2013:
        gry_po_2013.append(gra)

print("Gry wydane po 2013:")
pprint(gry_po_2013)

print("Zapis nowego pliku")
with open("l1_2.json", "w") as file:
    json.dump(spis_gier, file, indent=4, sort_keys=True)