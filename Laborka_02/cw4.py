a = float(input("Podaj liczbę: "))

if a > 0:
    print("Liczba ", a, " jest dodatnia")
elif a < 0:
    print("Liczba ", a, "  jest ujemna")
elif a == 0:
    print("Liczba ", a, "  jest zerem")

if a % 2 == 0:
    print("Liczba", a, " jest podzielna przez 2, czyli jest parzysta")
else:
    print("Liczba", a, " nie jest podzielna przez 2, czyli jest nieparzysta")