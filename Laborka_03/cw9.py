import random
liczby = []
while len(liczby) < 6:
    n = random.randint(1, 50)
    if n not in liczby:
        liczby.append(n)

print(liczby)