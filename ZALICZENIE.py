class Druzyna:
    def __init__(self, nazwa, sport, ilosc_osob):
        self.nazwa = nazwa
        self.sport = sport
        self.ilosc_osob = ilosc_osob

    def nazwa(self):
        print(f"Drużyna posiada nazwę {self.nazwa()}.")

    def sport(self):
        print(repr(f"Drużyna uprawia {self.sport()}."))

    def ilosc_str(self):
        print(f"Drużyna posiada {str(self.ilosc_osob)} osób.")

class Zawodnicy(Druzyna):
    def __init__(self, nazwa, sport, czy_ma_kota):
        super().__init__(nazwa, sport)
        self.czy_ma_kota = czy_ma_kota

    def kot(self):
        if self.czy_ma_kota == True:
            print(f"Zawodnicy mają kotów.")
        else:
            print(f"Zawodnicy nie mają kotków :(")

    def nazwa(self):
        super().nazwa()

#nowy kod
class Hotel:
    def __init__(self, ilosc_pokoi, parking, ilosc_miejsc_noclegowych, restauracja):
        self.ilosc_pokoi = ilosc_pokoi
        self.parking = parking
        self.ilosc_miejsc_noclegowych = ilosc_miejsc_noclegowych
        self.restauracja = restauracja
    def wolne_miejsca(self):
        print(f"Ten hotel posiada {self.ilosc_miejsc_noclegowych} wolnych miesjc.")
    def czy_park(self):
        if self.parking == True:
            print(f"Hotel posiada parking, możesz śmiało zostawić swoje auto.")
        else:
            print(f"Przykro mi, ale nie mamy parkingu.")

class Motel:
    def __init__(self, ilosc_pokoi, parking, ilosc_miejsc, sniadanie):
        self.ilosc_pokoi = ilosc_pokoi
        self.parking = parking
        self.ilosc_miejsc = ilosc_miejsc
        self.sniadanie = sniadanie
    def wolne_miejsca(self):
        print(f"Motel ma {self.ilosc_miejsc} wolnych miejsc i {self.ilosc_pokoi} pokoi w ogóle")

    def czy_park(self):
        print(f"Jasne, że motel ma swój parking. Ej ty, ciężarówkę dalej odstaw.")