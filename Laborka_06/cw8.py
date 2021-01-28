import random

jakasLista = random.sample(range(0,50), 10)

print("Zwykła lista: ", jakasLista)

random.shuffle(jakasLista)

print("Pomieszana lista: ", jakasLista)

jakasLista.sort()

print("Posortowana lista:", jakasLista)
