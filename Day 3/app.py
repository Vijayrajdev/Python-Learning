# constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
print(point1.x)

# constructors 2


class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, This is {self.name}")


John = Person("Jhon smith")
John.talk()

Bob = Person("Bob smith")
Bob.talk()

# Inheritance


class Mammal:

    def walk(self):
        print("Walk")


class Dog(Mammal):

    def Bark(self):
        print("Bark")


class Cat(Mammal):

    def Annoy(self):
        print("Annoying")


dog1 = Dog()
dog1.Bark()
dog1.walk()

cat1 = Cat()
cat1.walk()
cat1.Annoy()

# Modules

import converters

from converters import lbs_to_kg

converters.kg_to_lbs(100)
lbs_to_kg(99.99)

# Module Exercise

from utils import find_max

numbers = [12, 3, 4, 6, 7, 89]
maximum = find_max(numbers)
print(maximum)

# Packages
from ecommerce import shopping

shopping.shopping()

# python modules

import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 30))

choice = ["Vijay", "Raj", "Vishu", "devi"]
leader = random.choice(choice)
print(leader)

# Modules practice

import random


class Dice:

    def Roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second


dice = Dice()
print(dice.Roll())

# Path

from pathlib import Path

path = Path()

for file in path.glob("*"):
    print(file)



