def simple_conveyor():
    print("Starting engine..")
    yield "Book 1"
    print("Moving belt..")
    yield "Book 2"
my_belt = simple_conveyor()
result = next(my_belt)
result2 = next(my_belt)
result3 = next(my_belt)