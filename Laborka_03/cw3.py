a = []

for x in range(100, 200):
    if x % 2 != 0:
        if x % 2 != 0 and x % 3 != 0:
            a.append(x)

print(a)