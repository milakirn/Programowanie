class smartphone:
    def __init__(self, name, model, price,  battery, nr_telephone, memory, os, charged):
        self.name = name
        self.model = model
        self.price = price
        self.battery = battery
        self.nr_telephone = nr_telephone
        self.memory = memory
        self.os = os
        self.charged = charged

    def IsCharge(self):
        print(self.name, self.model, "jest ")
        if self.charged > 80:
            print("Naładowany")
        elif 80 > self.charged >= 50:
            print("Niezbyt naładowany")
        else:
            print("Rozładowany")

    def BasicStuff(self):
        print(self.name, " ", self.model)

    def Charge(self, charged):
        how_much = 0
        while how_much != charged:
            how_much += 5
            print("Naładowałeś do ", how_much, "procent")


smartphone1 = smartphone("Nokia", "3310", 0, 1600, "997998999", "32", "Symbian", 100)

smartphone2 = smartphone("Samsung", "Galaxy Note 7", 500, 3500, "999899799", "64", "Android", 50)

smartphone3 = smartphone("Xiaomi", "Redmi Note 8t", 800, 4000, "080978898", "64", "Android", 0)

smartphone3.IsCharge()
smartphone2.BasicStuff()
smartphone1.Charge(80)