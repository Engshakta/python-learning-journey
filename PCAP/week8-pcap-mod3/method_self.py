# class Car:
#     def __init__(self):
#         self.fuel = 100
    
#     def check_fuel(self):
#         print("Fuel is:", self.fuel)
    
#     def start_trip(self):
#         print("Starting...")
#         self.check_fuel()
    

# Method name mangling(Hidden access)

class Car:
    def __secret_engine_check(self):
        print("Engine is perfect.")

my_car = Car()


# This will CRASH with an AttributeError:
my_car.__secret_engine_check() 

# This works perfectly because of Name Mangling!


