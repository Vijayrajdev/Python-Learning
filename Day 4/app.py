# # Lambda function

# def operation(n):
#     return lambda a: a * n


# doubler = operation(2)
# tripler = operation(3)

# print(doubler(20))
# print(tripler(20))

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