menu = {
    "barszcz": 7,
    "schab": 10,
    "wino": 20,
    "ziemniaki": 4,
    "Browar" : 3
}
for nazwa, cena in menu.items():
    print(nazwa)
    print(cena)
    print(f"{nazwa} : {cena}")
KeyMin = min(menu, key=menu.get)
KeyMax = max(menu, key=menu.get)
print(f"/n")
print(KeyMin)
print(KeyMax)
print(f"/n")
del menu[KeyMin]
del menu[KeyMax]

print(menu)

menu["Hawajska"] = 19.99
print(menu)