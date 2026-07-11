import time
class Vehicle:
    def turn(self, left):
        self.change_direction(left, True)
        time.sleep(0.25)
        self.change_direction(left, False)


class TrackedVehicle(Vehicle):
    def change_direction(self, left, on):
        print("tracks:", left, on)
 

class WheeledVehicle(Vehicle):
     def change_direction(self, left, on):
             print("Wheels:", left, on)
 

my_car = WheeledVehicle()
my_car.turn(True)