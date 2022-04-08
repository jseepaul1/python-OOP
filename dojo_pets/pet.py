# implement __init__( name , type , tricks ):
# implement the following methods:
class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping. Energy: {self.energy}")
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Energy: {self.energy} Health: {self.health}")
        return self

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} is playing. Health: {self.health}")
        return self

# noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} is making a noise")
        return self
