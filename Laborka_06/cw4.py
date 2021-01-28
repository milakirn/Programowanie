import math

n = int(input("Podaj liczbę naturalną: "))

def DzielnikiWlasciwe(a):
  wynik = []
  for i in range(1, int(math.sqrt(a)) + 1):
    if (a % i == 0):
      wynik.append(i)
  for i in range(len(wynik) - 1, -1, -1):
    if (a / wynik[i] != wynik[i]):
      wynik.append(a // wynik[i])
  return wynik

wynik = DzielnikiWlasciwe(n)
for x in wynik:
  print(x, end=" ")