a = 3
b = 2
c = 2.5
okno = 1.1 * 1.4
drzwi = 0.89 * 2

v = a*b*c
pc = (2*(a*b))+(2*(a*c))+(2*(b*c))

print("Twój pokój ma: ", v, "m^3, lub: ", pc, "m^2")

ileokna = int(input("Podaj ile masz okien w pokoju: "))
iledrzwi = int(input("Podaj ile masz drzwi w pokoju: "))

pc2 = ((2*(a*b))+(2*(a*c))+(2*(b*c)))-((okno*ileokna)+(drzwi*iledrzwi))

print("Po poprawkach twój pokój ma powierzchnię: ", pc2, "m^2")