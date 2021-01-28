#Piąte
wys_m = int(input("Na jakiej wysokości lecimy? [W metrach]: "))
wys_km = wys_m / 1000

if wys_km < 5:
    print(f"{wys_km} km to za nisko!")
else:
    print(f"Na tej wysokości ({wys_km} km) jesteś już bezpieczny")