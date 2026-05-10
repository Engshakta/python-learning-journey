largest = None
smallest = None

while True:
    svalue = input("Enter a number: ")

    if svalue == "done":
        break

    try:
        fvalue = int(svalue)

    except:
        print("Invalid input")
        continue

    if largest is None or fvalue > largest:
        largest = fvalue

    if smallest is None or fvalue < smallest:
        smallest = fvalue

print("Maximum is", largest)