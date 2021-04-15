class Pojazd:
    def __init__(self, marka, model, cena, poj_silnika, paliwo, przebieg):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.poj_silnika = poj_silnika
        self.paliwo = paliwo
        self.przebieg = przebieg


class Samochod(Pojazd):
    def __init__(self, marka, model, cena, poj_silnika, paliwo, przebieg, ilosc_drzwi, poj_bagaznika):
        super().__init__(marka, model, cena, poj_silnika, paliwo, przebieg)
        self.ilosc_drzwi = ilosc_drzwi
        self.poj_bagaznika = poj_bagaznika

    def jaki_przebieg(self):
        print("Samochód marki {} ma przebieg {}".format(self.marka, self.przebieg))

    def rodzaj_paliwa(self):
        print("Do samochodu marki {} modelu {} jest potrzebna {}".format(self.marka, self.model, self.paliwo))


class Motor(Pojazd):
    def __init__(self, marka, model, cena, poj_silnika, paliwo, przebieg, ilosc_miejsc):
        super().__init__(marka, model, cena, poj_silnika, paliwo, przebieg)
        self.ilosc_miejsc = ilosc_miejsc

    def przebieg(self):
        print("Motor marki {} ma przebieg {}".format(self.marka, self.przebieg))

    def rodzaj_paliwa(self):
        print("Do motoru marki {} modelu {} jest potrzebna {}".format(self.marka, self.model, self.paliwo))



samochod1 = Samochod("Fiat", "124", "13000", "1.6", "benzyna", "250000", "4", "300l")
motor1 = Motor("Kawasaki", "Ninja", "7000", "650", "benzyna", "200000", "2")

samochod1.jaki_przebieg()
motor1.rodzaj_paliwa()
samochod1.rodzaj_paliwa()