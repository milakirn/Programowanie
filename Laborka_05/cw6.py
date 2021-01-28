import random
import time

t1 = time.time()
print("Witam w mojej grze")

num = random.randint(1, 100)
for i in range(0, 4):
    if i < 3:
        x = int(input("Zgaduj liczbę: "))
        if x > num:
            print("Podałeś za duza wartosc, probuj dalej")
        elif x < num:
            print("Podalesz za mala wartosc, próbuj dalej")
        else:
            print(f"Zgadles! Wyłosowana liczba była {num}")
            break
    else:
        print("Haha przegrales!")
        print(f"Wyosowana liczba była {num}")

