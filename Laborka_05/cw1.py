counter = 0
lista = []

n = int(input("Podaj ilość liczb: "))
while counter < n:
    a = int(input("Podaj te liczby: "))
    if a < 0:
        continue
    else:
        lista.append(a)
        counter += 1
print(lista)
srednia = (sum(lista)) / n
print(srednia)