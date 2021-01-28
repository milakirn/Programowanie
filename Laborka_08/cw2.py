import statistics
from collections import OrderedDict
kontakty = {
    "Andrzej" : 760548967,
    "Jan" : 758964158,
    "Michał" : 658942658,
    "Kuba" : 425978965,
    "Kacper" : 896545788,
    "Kamil" : 963598763,
    "Bartek" : 712145986,
    "Romek" : 698657863,
    "Adam" : 989699548,
    "Lukasz" : 857796489,
}
print(kontakty)

kontakty["Nowy_Andrzej"] = kontakty.pop("Andrzej")
kontakty["Nowy_Lukasz"] = kontakty.pop("Lukasz")
print(kontakty)

#del kontakty["Kamil"]
med = statistics.median_low(kontakty)
med2 = statistics.median_low(kontakty)
print(med)

print(med2)
print(kontakty)
#del kontakty["Bartek"]

print(kontakty)

kontakty.clear()
print(kontakty)

kontakty["Adam"] = 598762489
kontakty["Jacek"] = 987689513
kontakty["Duda"] = 125997658
kontakty["Mateusz"] = 111111111
print(kontakty)

lista = [(k,v) for k, v in kontakty.items()]
print(lista)

print(sorted(kontakty.items(), key = lambda kv:(kv[1], kv[0])))

dict1 = OrderedDict(sorted(kontakty.items()))
print(dict1)