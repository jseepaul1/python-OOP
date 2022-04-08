# Create a Ninja class with the ninja attributes listed above.
from cat import Cat


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
# walk() - walks the ninja's pet invoking the pet play() method

    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method

    def feed(self):
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method

    def bathe(self):
        self.pet.noise()
        return self


cat = Cat("Juliet", "cat", "jump", 88, 90)
argo = Ninja("Argo", "k", cat, "six fish", "fancy feast") # Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
argo.feed().walk().bathe()  # Have the Ninja feed, walk , and bathe their pet.
