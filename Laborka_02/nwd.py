def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    else:
        return a

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
print(nwd(a,b))