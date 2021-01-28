def silnia(liczba):
    wynik=1
    for licznik in range(2,liczba+1):
        #wynik=wynik*licznik
        wynik *= licznik
    return wynik
print (silnia(5))