pytanie = int(input("Jak chcesz skonwertować: (1 -F/C, 2 - C/F, 3 - F/K, 4 - K/F, 5 - C/K, 6 - K/C): "))

temperatura = int(input("Podaj temperaturę do przeliczenia w wybranych jednotkach: "))
def Fahr_Cels(temperatura):
    if pytanie == 1:
        wynik = (temperatura - 32)/1.8
    elif pytanie == 2:
        wynik = (temperatura * 1.8) + 32
    return round(wynik, 2)

def Fahr_Kel(temperatura):
    if pytanie == 3:
        wynik = (temperatura + 459.67) * 5/9
    elif pytanie == 4:
        wynik = (temperatura * 1.8) - 459.67
    return round(wynik, 2)

def Kel_Cels(temperatura):
    if pytanie == 5:
        wynik = (temperatura / 273.15)
    elif pytanie == 6:
        wynik = (temperatura + 273.15)
    return round(wynik, 2)

if pytanie == 1 or pytanie == 2:
    print(Fahr_Cels(temperatura))
elif pytanie == 3 or pytanie == 4:
    print(Fahr_Kel(temperatura))
elif pytanie == 5 or pytanie == 6:
    print(Kel_Cels(temperatura))