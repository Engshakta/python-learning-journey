class Vehicle:
    def start_engine(self):
        return "Vroom!"
    
class LandVehicle(Vehicle):
    def start_engine(self):
        parent_sound = super().start_engine()
        return parent_sound + "Rumble rumble ...Vrooom!"

my_car = LandVehicle()
print(my_car.start_engine())