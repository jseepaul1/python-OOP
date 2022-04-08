from pet import Pet
# NINJA BONUS: Use modules to separate out the classes into different files.
# SENSEI BONUS: Use Inheritance to create sub classes of pets.


class Cat(Pet):
    def noise(self):
        print(f"{self.name} is meowing")
        return self
