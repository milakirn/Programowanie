import random

orzel = 0
reszka = 0
for x in range(50):
    y = random.randint(0, 1)
    if y == 0:
        orzel += 1
    else:
        reszka += 1
print("Wylosowało {} orłów i {} reszek.".format(orzel, reszka))