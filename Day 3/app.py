# constructors
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")
    def draw(self):
        print("draw")


point1 = Point(10,20)
print(point1.x)

# constructors

class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, This is {self.name}")


John = Person("Jhon smith")
John.talk()

Bob = Person("Bob smith")
Bob.talk()
