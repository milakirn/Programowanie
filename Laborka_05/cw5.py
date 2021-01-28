szescian = [x**3 for x in range(101)]
print(szescian)
suma = sum(szescian)
print(suma)
warunek = 10**6
counter = 0
suma2 = 0
lista_liczb = []
for i in szescian:
    while suma2 <= warunek:
        lista_liczb.append(szescian[counter])
        suma2 += szescian[counter]
        counter += 1
print(lista_liczb)
print(len(lista_liczb))
print(suma2)