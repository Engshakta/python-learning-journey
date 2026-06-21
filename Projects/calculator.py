
def multiply_two_numbers():
    print("\n--- Multiplication ---")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    return num1 * num2

def add_two_numbers():
    print("\n--- Addition ---")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    return num1 + num2

def def_two_numbers():
    print("\n--- Difference ---")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    return num1 - num2

def div_two_numbers():
    print("\n--- Division ---")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    if num2 == 0:
        return "Error! Cannot divide by zero."
    return num1 / num2



print("___Calculator___")
while True:
    print("\n1. Multiplication of any two numbers")
    print("2. Addition of any two numbers")
    print("3. Difference of any two numbers")
    print("4. Division of any two numbers")
    print("5. Exit")
    
    choice = input("Please choose one of these options to use the calculator: ")

    if choice == "1":
        print(f"The multiplication of the two numbers is: {multiply_two_numbers()}")
    
    elif choice == "2":
        print(f"The addition of the two numbers is: {add_two_numbers()}")

    elif choice == "3":
        print(f"The difference of the two numbers is: {def_two_numbers()}")

    elif choice == "4":
        print(f"The division of the two numbers is: {div_two_numbers()}")
    
    elif choice == "5":
        print("Good bye!")
        break

    else:
        print("Invalid option, please choose from the options.")
