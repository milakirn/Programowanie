def Fahr_Cels(Cels):
    fahr = (Cels * 1.8) + 32
    if fahr <= 32:
        return (f"Temperatura w Fahrenheitach wynosi {fahr} stopni.\nPrzy temperaturze {round(fahr,2)} woda zamarza!\n")
    elif fahr >= 212:
        return (f"Temperatura w Fahrenheitach  wynosi {fahr} stopni.\nPrzy temperaturze {round(fahr,2)} woda wrze!\n")
    else:
        return (f"Temperatura w Fahrenheitach wynosi {fahr} stopni.")
def Cels_Fahr(Fahr):
    cels = (Fahr - 32) / 1.8
    return (f"Temperatura w Celsjuszach wynosi {round(cels, 2)} stopni\n")

def Fahr_Kelv(Kelv):
    fahr = (Kelv * 1.8) - 459.67
    return (f"Temperatura w Fahrenheitach wynosi {round(fahr,2)} stopni.\n")

def Kelv_Fahr(Fahr):
    kelv = (Fahr + 459.67) * 5/9
    return (f"Temperatura w Kelvinach wynosi {round(kelv,2)} stopni.\n")

def Kelv_Cels(Cels):
    kelv = (Cels + 273.15)
    return (f"Temperatura w Kelvinach wynosi {round(kelv, 2)} stopni.\n")

def Cels_Kelv(Kelv):
    cels = Kelv - 273.15
    return (f"Temperatura w Celsjuszach wynosi {round(cels, 2)} stopni.\n")

def Rank(na_z, rodzaj, temperatura):
    if na_z.lower() == "na":
        if rodzaj.upper() == "C":
            return (temperatura / 1.8) - 273.15
        elif rodzaj.upper() == "K":
            return (temperatura * 5/9)
        elif rodzaj.upper() == "F":
            return (temperatura - 459.67)
    elif na_z.lower() == "z":
        if rodzaj.upper() == "C":
            return (temperatura + 273.15) *1.8
        elif rodzaj.upper() == "K":
            return (temperatura * 9/5)
        elif rodzaj.upper() == "F":
            return (temperatura + 459.67)

if __name__ == "__main__":
    cels = int(input("Podaj temperature w Celsjuszach: "))
    print(Fahr_Cels(cels))
    print(Kelv_Cels(cels))

    kelv = int(input("Podaj temperature w Kelvinach: "))
    print(Cels_Kelv(kelv))
    print(Fahr_Kelv(kelv))

    fahr = int(input("Podaj temperature w Fahrenheitach: "))
    print(Kelv_Fahr(fahr))
    print(Cels_Fahr(fahr))

    pytanie = input("Czy chcesz zobaczyć przeliczenie Rank? ")
    if pytanie.upper() == "TAK":
        pyt2 = input("Chcesz przeliczyć na Rankine czy z Rank? (na, z) ").lower()
        if pyt2 == "na":
            pyt3 = int(input("Podaj temperature: "))
            print(f"Temperatura w Rankinach z Celsjuszy wynosi {round(Rank('na','C',pyt3),2)} stopni\n")
            print(f"Temperatura w Rankinach z Kelvinów wynosi {round(Rank('na', 'K', pyt3),2)} stopni\n")
            print(f"Temperatura w Rankinach z Fahrenheitów wynosi {round(Rank('na', 'F', pyt3))} stopni\n")
        elif pyt2 == "z":
            pyt3 = int(input("Podaj temperature: "))
            print(f"Temperatura w Celsjuszach wynosi {round(Rank('z','C',pyt3),2)} stopni\n")
            print(f"Temperatura w Kelvinach wynosi {round(Rank('z', 'K', pyt3),2)} stopni\n")
            print(f"Temperatura w Fahrenheitach wynosi {round(Rank('z', 'F', pyt3))} stopni\n")

    else:
        print("Koniec programu")