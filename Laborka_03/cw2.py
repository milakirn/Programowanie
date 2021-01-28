n = int(input("Podaj liczbe: "))
a = []
for x in range(n, 0, -1):
    if x % 6 == 0 and x % 9 == 0:
      a.append(x)
print(a)