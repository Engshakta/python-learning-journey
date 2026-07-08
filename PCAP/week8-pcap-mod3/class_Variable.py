class Car:
    counter = 0
    def __init__(self,color):
        self.color = color
        Car.counter += 1

car_1 = Car("Red")
car_2 = Car("Blue")
car_3 = Car("Silver")

print("Car 1 backpack:", car_1.__dict__, "Factory counter:", car_1.counter)
print("Car 2 backpack:", car_2.__dict__, "Factory counter:", car_2.counter)
print("Car 3 backpack:", car_3.__dict__, "Factory counter:", car_3.counter)