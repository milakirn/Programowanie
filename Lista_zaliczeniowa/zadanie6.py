def Fahr_Cels(Cels):
    fahr = (Cels * 1.8) + 32
    if fahr <= 32:
        print(f"Przy temperaturze {round(fahr,2)} woda zamarza!")
    elif fahr >= 212:
        print(f"Przy temperaturze {round(fahr,2)} woda wrze")
    else:
        print(f"Temperatura wynosi {fahr} stopni.")

def Fahr_Kelv(Kelv):
    fahr = (Kelv * 1.8) - 459.67
    print(f"Temperatura w Fahrenheitach wynosi {round(fahr,2)}")

def Kelv_Fahr(Fahr):
    kelv = (Fahr + 459.67) * 5/9
    print(f"Temperatura w Kelvinach wynosi {round(kelv,2)}")

def Kelv_Cels(Cels):
    kelv = (Cels + 273.15)
    print(f"Temperatura w Kelvinach wynosi {round(kelv, 2)}")

def Cels_Kelv(Kelv):
    cels = Kelv - 273.15
    print(f"Temperatura w Celsjuszach wynosi {round(cels, 2)}")

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

#if __name__ == "__main__":
    cels = int(input("Podaj temperature w Celsjuszach: "))
    print(Fahr_Cels(cels))

if __name__ == "__main__":
    pytanie = input("Czy chcesz zobaczyć przeliczenie Rank? ")
    if pytanie.upper() == "TAK":
        pyt2 = input("Chcesz przeliczyć na Rankine czy z Rank? (na, z) ").lower()
        if pyt2 == "na":
            rodzaj = input("Wybierz typ temperatury: (C, F, K) ").upper()
            pyt3 = int(input("Podaj temperature: "))
            if rodzaj == "C":
                print(f"Temperatura w Rankinach wynosi {round(Rank('na',rodzaj,pyt3),2)}")
            elif rodzaj == "K":
                print(f"Temperatura w Rankinach wynosi {round(Rank('na', rodzaj, pyt3),2)}")
            elif rodzaj == "F":
                print(f"Temperatura w Rankinach wynosi {round(Rank('na', rodzaj, pyt3))}")
        elif pyt2 == "z":
            rodzaj = input("Wybierz typ temperatury: (C, F, K)").upper()
            pyt3 = int(input("Podaj temperature: "))
            if rodzaj == "C":
                print(f"Temperatura w Celsjuszach wynosi {round(Rank('z',rodzaj,pyt3),2)}")
            elif rodzaj == "K":
                print(f"Temperatura w Kelvinach wynosi {round(Rank('z', rodzaj, pyt3),2)}")
            elif rodzaj == "F":
                print(f"Temperatura w Fahrenheitach wynosi {round(Rank('z', rodzaj, pyt3))}")
