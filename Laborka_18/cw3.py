import random

stos = []
kolejka = []

for i in range(50):
    stos.append(random.randint(0,100))

print("Stos: ", stos)

for elements in stos:
    kolejka.insert(0, elements)

print("Kolejka: ", kolejka)