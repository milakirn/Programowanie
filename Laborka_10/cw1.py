stringers = f"""Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć zakazane drzwi. Drzwi, za którymi czai się koszmar, 

zgroza i niewyobrażalna okropność, za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nie tylko tego, kto drzwi 

te uchyli, ale i cały świat. A ponieważ nie brakuje takich, którzy przy owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada 

świata będzie przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po Koniunkcji Sfer ludzie nauczyli posługiwać się magią, 

jest przekleństwem i zgubą świata. Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się"""

print("Lower")

print(stringers.lower())

print("Swapcase")

print(stringers.swapcase())

print("Capitalize")

print(stringers.capitalize())

print("Replace")

print(stringers.replace("."," !@^%*&^% "))

print("Lstrip")

print(stringers.lstrip())

print("Rstrip")

print(stringers.rstrip())

print("Reversed")

print(stringers[::-1])

print("Count : y pojawia się tyle razy: ")

print(stringers.count("y",0,len(stringers)))

print("Find")

print(stringers.find("Zaraza",0,len(stringers)))

print("Isallnum")

print(stringers.isalnum())

print("Startswith")

print(stringers.startswith("Magia",0,len(stringers)))

print("Endswith")

print(stringers.endswith("Chaosu",0,len(stringers)))