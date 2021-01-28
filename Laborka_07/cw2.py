import random
num_even = []
num_odd = []
lista = []
for i in range(100):
    lista.append(random.randint(0,10))
tup = tuple(lista)
print(tup)
print(tup.count(0))
print(tup.count(1))
print(tup.count(2))
for i in tup:
    if i % 2 == 0:
        num_even.append(i)
    else:
        num_odd.append(i)
print(f"Liczby parzyste {num_even}")
print(f"Liczby nieparzyste {num_odd}")
