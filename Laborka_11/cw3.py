import math
kat = int(input("Podaj kąt w stopniach: "))
sin = round(math.sin(kat), 3)
cos = round(math.cos(kat), 3)
tan = round(math.tan(kat), 3)
ctg = 0
try:
    ctg = round(1 / tan, 3)
except ZeroDivisionError:
    print("Nie ma takiego znaczenia")

print(f"Dla kąta {kat} stopni wartości funkcji trygonometrycznych wynoszą {sin, cos, tan, ctg}")