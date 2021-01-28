import random
tab = []
for x in range(10):
    b = random.randint(0,59)
    tab.append(b)
print(tab)

tab.append(14)
tab.insert(4,16)
tab.append(42)

print(tab)

tab.pop(5)
tab.pop(7)
try:
    tab.remove(3)
except ValueError:
    print("Nie ma takiego indexu")

print(tab)

tab[4] = 3
tab[9] = 33

print(tab)