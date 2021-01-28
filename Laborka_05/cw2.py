import statistics

n = int(input("Podaj początek zakresu: "))
x = int(input("Podaj koniec zakresu: "))

if n == 0 or x == 0:
    print("Koniec programu")
else:
    lista = []
    for a in range(n,x+1):
        lista.append(a)
    print(lista)

    lista_cal = lista[0:6]

    print(lista_cal)
    while True:
        print(min(lista_cal))
        print(max(lista_cal))
        print(sum(lista_cal))
        print(statistics.median(lista_cal))
        break