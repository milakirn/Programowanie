class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Cena wynosi {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#zmiana ceny
c.__maxPrice = 3000
c.sell()

#używamy settera
c.setMaxPrice(4000)
c.sell()