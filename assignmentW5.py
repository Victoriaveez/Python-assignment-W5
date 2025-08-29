# Base class
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        print(f"I am {self.name}, and my power is {self.power}.")

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

# Subclass 1
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} flies through the sky with {self.power}!")

# Subclass 2
class StrongHero(Superhero):
    def use_power(self):
        print(f"{self.name} lifts a car with their {self.power}!")

# Create objects
hero1 = FlyingHero("SkyWing", "flight")
hero2 = StrongHero("RockFist", "super strength")

# Use methods
hero1.introduce()
hero1.use_power()

print()  # Just a space

hero2.introduce()
hero2.use_power()
