class Car:
    def __init__(self, color):
        self.color = color

    def add_spoiler(self):
        self.spoiler = True

car_1 = Car("Red")
car_2 = Car("Blue")

car_2.add_spoiler()

car_1.headlights = "LED"

print("Car 1 Features: ", car_1.__dict__)
print("Car 2 Features: ", car_2.__dict__)