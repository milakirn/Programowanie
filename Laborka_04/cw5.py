sum = 0
sr = 0
cos = True

while cos:
    a = int(input("Podaj a: "))
    sum += a
    print(sum)
    c = (a + sum) / 2
    sr += c
    print(sr)
    if sum > 100 or sr == 66:
        print("Suma wynosi ", sum," oraz średnia wynosi ", sr)
        cos = False

