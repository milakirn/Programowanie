n = int(input("podaj: "))
ciag = []
ciag.append(n)
while n != 1:
    if (n-1) %2 == 0:
        n = n // 2
        print(ciag)
    else:
        n = 2 * n + 1
        print(ciag)
    ciag.append(n)
print(ciag)