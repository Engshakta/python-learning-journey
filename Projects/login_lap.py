def login_system():
    # define the correct credentials
    correct_username = "admin"
    correct_password = "admin123"

    print("---- Welcome to the System -----")

    # get input from the user
    username_input = input("Enter your username please: ")
    password_input = input("Enter your password please:")

    # check if the credetials match

    if username_input == correct_username and password_input == correct_password :
        print("\n Login successful! welcome back.")
    else:
        print("\nLogin failed! invalid username or password.")

# Run the program

login_system()