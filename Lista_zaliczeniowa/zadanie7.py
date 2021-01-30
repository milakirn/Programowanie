import datetime

def czy_przestepny(r):
    if r % 4 == 0 and r % 100 != 0 or r % 400 == 0:
        return True
    else:
        return False

def dzien_miesiac(r):
    luty = 28
    if czy_przestepny(r):
        luty = 29
    miesiace = [31, luty, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return miesiace

def jutro(d, m, r):
    miesiace = dzien_miesiac(r)
    rok_jutro = r
    miesiac_jutro = m
    dzien_jutro = d + 1
    if dzien_jutro > miesiace[m - 1]:
        miesiac_jutro = m + 1
        if miesiac_jutro > 12:
            rok_jutro = r + 1
            miesiac_jutro = 1
        dzien_jutro = 1
    return (dzien_jutro, miesiac_jutro, rok_jutro)

def wczoraj(d, m, r):
    miesiace = dzien_miesiac(r)
    rok_wczor = r
    mies_wczor = m
    dzien_wczor = d - 1
    if dzien_wczor == 0:
        mies_wczor = m - 1
        if mies_wczor == 0:
            rok_wczor = r - 1
            mies_wczor = 12
            dzien_wczor = 31
        else:
            dzien_wczor = miesiace[mies_wczor - 1]
    return (dzien_wczor, mies_wczor, rok_wczor)

def wielkanoc(y):
    a = (y % 19)
    b = (y % 4)
    c = (y % 7)
    d = ((19 * a + 24) % 30)
    e = ((2 * b + 4 * c + 6 * d + 5) % 7)
    marday = (22 + d + e)
    aprday = (d + e - 9)
    if marday > 31:
        return (aprday, 4, y)
    else:
        return (marday, 3, y)

def data(d, m, r):
    wczor = wczoraj(d, m, r)
    print(f"Wczoraj było: {wczor}")
    tommor = jutro(d, m, r)
    print(f"Jutro będzie: {tommor}")
    sw = wielkanoc(r)
    print(f"Wielkanoc wypada w: {sw}")
    dni = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    dzienn = datetime.date(r, m, d)
    dzienn_tyg = dzienn.weekday()
    dzienn_tyg_str = dni[dzienn_tyg]
    return (f"Dzień tygodnia dla {d}.{m}.{r} to {dzienn_tyg_str}")

if __name__ == "__main__":
    dz = int(input("Podaj dzień: "))
    mies = int(input("Podaj miesiąc: "))
    rok = int(input("Podaj rok: "))
    print(data(dz, mies, rok))