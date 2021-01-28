import statistics
lista1 = [3,5,3,12,13,3,7,8]
lista2 = [3,3,3,5,7,8,12,13]
print(statistics.median(lista1))
print(lista1)
print(statistics.median_low(lista1))
print(statistics.median(lista2))
print(lista2)
print(statistics.median_low(lista2))
print(statistics.median_high(lista1))
print(lista2[(statistics.median_high(lista2))])

l2 = ["bla", "aga"]
l2[0] = 0
print(l2)