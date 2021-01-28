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

