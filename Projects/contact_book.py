contact_book = {}

print("____ This is contact book____")

while True:
    print("\n1. Enter to add a new contact")
    print("2. Enter to find an existing contact")
    print("3. Enter to update an existing contact")
    print("4. Enter to delete a contact")
    print("5. Exit")

    choice = input("Please Enter an option to choose: ")

    if choice == '1':
        name = input("Enter the name of the contact person: ")
        number = input("Enter the number of the contact person: ")
        contact_book[name] = number
        print(f"The contact: {name} with number {number} is added successfully.")
        
    elif choice == '2':
        name = input("Enter contact name: ")
        if name not in contact_book:
            print("Contact doesn't exist.")
        else:
            print("The number is", contact_book[name])

    elif choice == '3':
        name = input("Enter the name of the contact person you want to update: ")
        if name not in contact_book:
            print("You can't update non-existent contact.")
        else:
            while True:
                print("\nA. Update only the name")
                print("B. Update only the number")
                print("C. Exit updating menu")

                updating_choice = input("Please Enter an option you want to update: ").upper()
                if updating_choice == 'A':
                    new_name = input("Enter new name: ")
                    contact_book[new_name] = contact_book[name]
                    del contact_book[name]
                    name = new_name  # Fixes the crash by updating the tracking variable
                    print("Name updated successfully.")
                elif updating_choice == 'B':
                    new_number = input("Enter new number: ")
                    contact_book[name] = new_number
                    print("Number updated successfully.")
                elif updating_choice == 'C':
                    break
                else:
                    print("Invalid option. Please choose the listed options only.")
       
    elif choice == '4':   
        name = input("Enter the name of the contact person you want to delete: ")
        if name not in contact_book:
            print("You can't delete non-existent contact.")
        else:
            deleted_number = contact_book[name]
            del contact_book[name]
           
            print(f"The contact: {name} with number {deleted_number} is deleted successfully.")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Wrong choice, please choose only from the options.")
