def obliczanie_netto(brutto):
    emeryt = 0.0976 * brutto
    rentowa = 0.015 * brutto
    chorobowe = 0.0245 * brutto
    suma_skladek = emeryt + rentowa + chorobowe
    skladka_podstawowa = brutto - suma_skladek
    skladka_zdrowotna = skladka_podstawowa * 0.09
    part = suma_skladek + skladka_zdrowotna
    prawie_calosc =  brutto - part
    zus = skladka_podstawowa * 0.0775
    zaliczka = prawie_calosc * 0.17 - 43.76 - zus  #kwota 43.76 jest ustalona ustawowo
    if zaliczka < 0:
        zaliczka = 0
    return round((brutto - (zaliczka + part)), 2)

if __name__ == "__main__":

    kwota = float(input("Podaj swój zarobek brutto: "))
    print(f"Twój zarobek netto wynosi {obliczanie_netto(kwota)} złotych")
    kradziez = kwota - obliczanie_netto(kwota)
    print(f"Państwo zabiera u Ciebie {kradziez} złotych!")