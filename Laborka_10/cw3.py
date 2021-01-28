tekst = f"Długo na szturm i szaniec pogłądał w miłczeniu. Na koniec rzekł" \
        f": 'Stracona'."
tekst1 = tekst[:(tekst.find(".", 0,len(tekst)-1))]

print(tekst1)

lista1 = ["Zwinny", 'lis','przeskoczył','nad','leniwym','psem','.']

lista2 = lista1[0:len(lista1) - 2]
kropka = "."

listToString = ' '.join(map(str, lista2))
calosc = listToString + kropka
print(calosc)