import random

tab = []

for x in range(50):
    a = random.randint(1,100)
    tab.append(a)
print(tab)

tab = list(dict.fromkeys(tab))
print(tab)
print(len(tab))
