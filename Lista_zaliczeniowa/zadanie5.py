def przelicznik(kwota, typ, czy_na_dollar): #CENY PRZELICZENIA NA 29.01.2021 12:36
    przelicznik = {
        "THB" : 0.33,
        "BTC" : 37233.02,
        "BTN" : 0.014,
        "MRO" : 0.028,
        "ETH" : 1430.92,
        "UAH" : 0.036 #Ukraińska hrywnia
    }
    if typ in przelicznik:
        if czy_na_dollar == True:
            return kwota / przelicznik[typ]
        else:
            return kwota * przelicznik[typ]

if __name__ == "__main__":
    kwerenda = input("Chcesz zamienić dollary na inne(TAK), czy na dollary(NIE)? ").upper()
    if kwerenda == "TAK":
        kwota  = float(input("Ile chcesz wymienić dollarów? "))
        waluta = input("Na jaką walutę wymieniamy? (THB, BTC, BTN, MRO, ETH, UAH) ").upper()
        print(f"{kwota} $ to {round(przelicznik(kwota, waluta, True), 2)} {waluta}")
    else:
        waluta = input("Jaką walute masz przy sobie? (THB, BTC, BTN, MRO, ETH, UAH) ").upper()
        kwota = float(input("Jaką kwotę masz? "))
        print(f"{kwota} {waluta} to {round(przelicznik(kwota, waluta, False),2)} $")