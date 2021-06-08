class Znaki(Exception):
    def __init__(self, text):
        self.txt = text


class Kreska(Exception):
    def __init__(self, text):
        self.txt = text


a = input("Podaj kod pocztowy: ")
try:
    if len(a) != 6:
        raise Znaki("Kod ma miec 6 znakow!")
    if a[2] != '-':
        raise Kreska("Poprawny format kodu: 99-999")
except ValueError:
    print("Error type of value!")
except Znaki as zn:
    print(zn)
except Kreska as kr:
    print(kr)
else:
    f = open("Kod_pocztowy.txt", "a")
    f.write(a)
    f.write("\n")
    f.close()
