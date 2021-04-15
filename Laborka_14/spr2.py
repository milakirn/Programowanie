class Ja:
    def __init__(self, age = 18):
        self._age = age

    #getter
    def get_age(self):
        return self._age

    #setter
    def set_age(self, x):
        self._age = x

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)

stan = Ja()
'''#ustawiamy wiek za pomocą settera
stan.set_age(100)

#używamy gettera do zwrócenia wyniku
print(stan.get_age())

print(stan._age)
'''
stan.age = 100

print(stan.age)