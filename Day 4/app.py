# Lambda function

def operation(n):
    return lambda a: a * n


doubler = operation(2)
tripler = operation(3)

print(doubler(20))
print(tripler(20))

# Polymorphism

class car:
    def __init__(self,brand,model):
       self.brand = brand
       self.model = model

    def move(self):
        print("Drive!")

class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class airship:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = car("Tesla", "S3")
boat1 = boat("Ibiza", "Touring 20");
airship1 = airship("Boeing", "747")


for x in (car1, boat1, airship1):
    x.move()

# Math module

import math
a = 20
b = 10


print(min(a, b))
print(max(a, b))

print(math.sqrt(a))
print(math.pow(a, b))

# JSON

import json

Data = {
    "name": "Vijay",
    "age": 21,
    "married": False,
    "divorced": False,
    "children": None,
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

J_data = json.dumps(Data, indent=4, separators=(". ", " = "), sort_keys=True)

print(J_data)

# File handling

file = open(
    "C:\Vijay -STORAGE\Project\Python\Python-Learning\Day 4\demo.txt", "r")
print(file.read())
file.close()

# append content in file

file = open("Day 4\demo.txt", "a")
file.write("\nNow this file has one more content.")
file.close()

file2 = open("Day 4\demo.txt", "r")
print(file2.read())
file2.close()

file3 = open("Day 4\demo2.txt", "x")
file3.write("This is the new file!")
file3.close()

import os

os.remove("Day 4\demo2.txt")



# userchange