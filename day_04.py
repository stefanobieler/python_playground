class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

    def make_sound(self):
        pass


class Dog(Animal):

    def get_leg_count():
        return 4

    def make_sound(self):
        print(f"{self.name}: woof!")


class Cat(Animal):

    def make_sound(self):
        print(f"{self.name}: meow!")

    pass



spot = Dog("spot", 23)
jimmy = Cat("jimmy", 10)

spot.make_sound()
jimmy.make_sound()

timmy: Animal = Dog("timmy", 1)


print(Dog.get_leg_count())


print(spot.name)
print(spot.age)
print()
print(jimmy.name)
print(jimmy.age)

def attack(attacker: Animal, defender: Animal):
    pass


attack(spot, jimmy)