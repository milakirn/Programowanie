import math
#równanie kwadratowe

#y = ax**2 + bx + c

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a == 0:
    x = -c / b
    print(round((x), 2))
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = ((-b) - math.sqrt(delta)) / (2 * a)
        x2 = ((-b) + math.sqrt(delta)) / (2 * a)
        print("Rozwiązaniami są liczby ", round(x1, 2), round(x2, 2))
    elif delta == 0:
        x0 = (-b) / (2 * a)
    elif delta < 0:
        print("Równanie nie ma rozwiązań")