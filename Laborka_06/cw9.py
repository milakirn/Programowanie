n = int(input("Podaj ilość liczb: "))

tab = []
for x in range(n):
    a = int(input("Wpisz te liczby: "))
    tab.append(a)

print(tab)
maks = max(tab)
print(f"Maksymalna liczba jest {maks}")
print(f" Liczba {maks} występuje {tab.count(maks)} razy")
