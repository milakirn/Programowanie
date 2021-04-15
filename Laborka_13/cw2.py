class Book:
    def __init__(self, autor, tytul, rok_wydania, wydawnictwo, ilosc_stron):
        self.autor = autor
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.wydawnictwo = wydawnictwo
        self.ilosc_stron = ilosc_stron

    def SayMyName(self):
        print(self.autor)
        print(self.tytul)
        print(self.rok_wydania)
        print(self.wydawnictwo)
        print(self.ilosc_stron)

ksiazki = []
outsider = Book("King Stephen", "Outsider", 2018, "Charles Scribner`s Son", 560)

ksiazki.append(outsider)
def Main():
    print("Witaj!")
    Wybor()
    while True:
        opcja = input("Czy chcesz kontynuować operację? TAK / NIE")
        if opcja.upper() == "TAK":
            Wybor()
        elif opcja.upper() == "NIE":
            break

def Wybor():
    wybor = input("Witaj w księgarnie! Czy chcesz dodać książkę lub wyświetlić? ")
    if wybor == "1":
        dodaj_kszk()
    elif wybor == "2":
        pokaz_kszk()

def dodaj_kszk():
    autor = input("Podaj autora: Nazwisko Imie ")
    tytul = input("Podaj tytul: ")
    rok_wydania = input("Podaj rok wydania książki: ")
    wydawnictwo = input("Podaj wydawnictwo: ")
    ilosc_stron = input("Podaj liczbę stron w książce: ")

    book = Book(autor, tytul, rok_wydania, wydawnictwo, ilosc_stron)
    print(book.SayMyName())
    ksiazki.append(book)
    print("Dodano nową książkę!")

def pokaz_kszk():
    ksiazki.sort(key = Sort)
    for i in ksiazki:
        i.SayMyName()

def Sort(obj):
    z_czego = input("Jak chcesz posortować? autor / tytul / rok / wydawnictwo / ilosc stron")
    if z_czego.lower == "autor":
        return obj.autor
    elif z_czego.lower == "tytul":
        return obj.tytul
    elif z_czego.lower == "rok":
        return obj.rok_wydania
    elif z_czego.lower == "wydawnictwo":
        return obj.wydawnictwo
    elif z_czego.lower == "ilosc_stron":
        return obj.ilosc_stron
Main()
