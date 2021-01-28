from zadanie1 import obliczanie_netto

def koszt_pracodawcy(zarob_brutto):
    emeryt = zarob_brutto * 0.0976
    rentowe = zarob_brutto * 0.065
    wypadki = zarob_brutto * 0.0167
    fundacja = zarob_brutto * 0.0245
    fgsp = zarob_brutto * 0.01
    calosc = emeryt + rentowe + wypadki + fundacja + fgsp
    return zarob_brutto + calosc

if __name__ == "__main__":
    brutto = float(input("Podaj zarobek brutto: "))
    print(f"Lącznie pracodawca wydał na Ciebie {koszt_pracodawcy(brutto)} złotych.")
    print(f"Twój zarobek netto wynosi {obliczanie_netto(brutto)} złotych.")