class bird:
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def fly(self):
        print("Tu", self.gatunek, ".Lecimy i osiągamy prędkość", self.szybkosc)

class eagle(bird):

    def __init__(self,szybkosc):
        super().__init__("orzeł", szybkosc)

    def attack(self):
        print("Tu", self.gatunek,". Do atakuuuu!")

bir1 = eagle(200)
bir1.attack()
orzel = eagle(90)
orzel.fly()
orzel.attack()


class penguin (bird):
    def __init__(self, szybkosc):
        super().__init__("pingwin", szybkosc)

    def slide(self):
        print("Tu", self.gatunek,". Bziuuum")

    def fly(self):
        print("Tu", self.gatunek,". Nie potrafię latać:((")

ptak1 = penguin(25)
ptak1.slide()
pingwin = penguin(40)
pingwin.slide()
pingwin.fly()

class kukulka (bird):

    def __init__(self, szybkosc):
        super().__init__("Kukulka", szybkosc)

    def latanko (self):
        print("Tu ",self.gatunek,". Latam sobie latam!")

    def jajeczko (self):
        print("Znów ",self.gatunek,"! Widze gniazdo więc podrzucam tam jajka O")

kukulka = kukulka(34)
kukulka.latanko()
kukulka.jajeczko()