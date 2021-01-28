a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
c = float(input("Podaj liczbę c: "))

if a > b and a > c:
    print("LIczba ", a, "jest największa")
elif b > a and b > c:
    print("LIczba ", b, "jest największa")
elif c > a and c > b:
    print("LIczba ", c, "jest największa")
elif a == b == c:
    print("Wszystkie liczby takie same")