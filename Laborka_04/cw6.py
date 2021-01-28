def sumadzielinkow(n):
    suma = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            suma += i
    return suma

def doskonala(n):
    return sumadzielinkow(n) == n


def doskonala1000():
    lista = [n for n in range(1, 1000) if doskonala(n)]
    return lista

print (doskonala1000())
# [6, 28, 496]