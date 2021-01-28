import random
A = []
b = []
c = []

for i in range(100):
    a = random.randint(0, 10)
    A.append(a)

print(A)

tuple = tuple(A)
print("Liczba 0 występuje:", tuple.count(0) ,"razy")
print("Liczba 1 występuje:", tuple.count(1) ,"razy")
print("Liczba 2 występuje:", tuple.count(2) ,"razy")
for i in tuple:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

print("Parzyste: ", b)
print("Liczba parzysta występuje:", len(b) ,"razy")
print("Nieparzyste: ", c)
print("Liczba nieparzysta występuje:", len(c) ,"razy")