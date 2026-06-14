# 1. Animal -> Dog with super()
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent constructor
        super().__init__(name, "Woof")
        self.breed = breed

    def describe(self):
        print(f"{self.name} is a {self.breed}")

a = Animal("Cat", "Meow")
d1 = Dog("Buddy", "Labrador")
d2 = Dog("Rex", "Beagle")
a.speak()
d1.speak() 
d1.describe() 
d2.speak()
d2.describe() 