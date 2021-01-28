import random

tab1 = []
tab2 = []
powt = 0

x = int(input("Podaj początek zakresu: "))
z = int(input("Podaj koniec zakresu: "))

for a in range(x,z + 1):
    y = random.randint(x,z)
    tab1.append(y)
print(tab1)
print(tab1[-3])

k = int(input("Podaj element, który chcesz usunąć: "))
tab1.pop(k + 1)

for a in range(x,z):
    y = random.randint(x,z)
    tab2.append(y)

tabsum = tab1 + tab2
print(tabsum)

for i in range(len(tabsum) + 1):
    if tabsum.count(i) > 1:
        powt += 1
    i += 1

print(len(tabsum))
print(powt)