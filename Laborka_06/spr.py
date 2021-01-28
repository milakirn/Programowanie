import random

first = int(input("Podaj pierwszą liczbę z zakresu:"))

last = int(input("Podaj ostatnią licbę z zakresu:"))

tab = []

i=0

while i != last:

   tab.append(random.randint(first, last))

   i += 1

print(tab)

tab = list(dict.fromkeys(tab))

print(tab)

print("Długość listy:", len(tab))