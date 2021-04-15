class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
class Cat(Animal):
    def __init__(self,name, type, food, pet_name):
        super().__init__(name, type)
        self.food = food
        self.pet_name = pet_name
    def printfood(self):
        print("Kot lubi:", self.food)

    def printpetname(self):
        print("A jego imię to: ", self.pet_name)

cat1 = Cat("cat", "MaineCoon", "Whisky","Jack")
cat1.printfood()
cat1.printpetname()