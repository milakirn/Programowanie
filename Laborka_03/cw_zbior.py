import random
print("1 - LOTTO")
print("2 - Multi Muti")
print("3 - Mini LOTTO")
a = int(input("Wybierz rodzaj losowania :"))
liczby = []
n = 0
if a == 1:
    for i in range(0,6):
        n = random.randint(1, 50)
        liczby.append(n)
        print("Twoje liczby to:", n)
if a == 2:
    for i in range(0, 20):
        n = random.randint(1, 80)
        liczby.append(n)
        print("Twoje liczby to:", n)
if a == 3:
    for i in range(0,5):
        n = random.randint(1, 42)
        liczby.append(n)
        print("Twoje liczby to:", n)
print("Dziękujemy za grę :) i twoje pieniadze")