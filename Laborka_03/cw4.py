a = []
for x in range (100, 201):
    if x % 2 == 0:
        if x % 6 != 0 and x % 5 != 0 and x % 11 != 0:
            a.append(x)
print(a)