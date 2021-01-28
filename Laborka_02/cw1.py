a = int(input("podaj pierwszą liczbe: "))
b = int(input("podaj drugą liczbe: "))
z = (a / b)
if int(z) == a / b:
    print("{} jest podzielne przez {}".format(a, b))
else:
    print("{} nie jest podzielne przez {}".format(a, b))