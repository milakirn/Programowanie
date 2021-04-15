class Student:
    def __init__(self, imie, nazwisko, plec, pesel, uczelnia, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.pesel = pesel
        self.uczelnia = uczelnia
        self.kierunek = kierunek

    def dane_osobowe(self):
        return f"Student o numerze PESEL {self.pesel} nazywa się {self.imie} {self.nazwisko}."

    def studia(self):
        return "{} {} uczy się w {} na kierunku {}.".format(self.imie, self.nazwisko, self.uczelnia, self.kierunek)

student1 = Student("Andrzej", "Duda", "Mężczyzna", 5497536214, "PWr", "Analiza danych")
student2 = Student("Jan", "Paweł", "Mężczyzna", 54896235478, "Kościoł Św.Joanny", "Ateizm")

print(student2.studia())
print(student1.dane_osobowe())