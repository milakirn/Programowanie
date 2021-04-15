class Parrot:
    species =  "ptak"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return f"{self.name} spiewa {song}"

    def dance(self):
        return f"{self.name} tanczy"

blu = Parrot("Blu", 10)
ara = Parrot("Ara", 15)

print(f"Blu jest {blu.__class__.species}")
print(f"Ara jest {ara.__class__.species}")

print(blu.sing("Happy"))
print(blu.dance())
print(ara.dance())