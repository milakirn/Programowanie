a = int(input("Podaj liczbę: "))

if a <= 10:
    print("Liczba ", a, " jest mniejsza lub jest równa 10")
elif a > 10 and a <= 25:
    print("Liczba ", a, " jest większa od 10 i mniejsza od 25")
else:
    print("Liczba ", a, " jest większa od 25")