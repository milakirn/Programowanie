miesiace = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik"
            , "listopad", "grudzien"]
while True:
    inp = int(input("Proszę podaj numer miesiaca: "))
    if inp == 0:
        print("Proszę podaj numer od 1 do 12")
        continue
    try:
        print(miesiace[inp-1])
        break
    except:
        print("Proszę podaj numer od 1 do 12")