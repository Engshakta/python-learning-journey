print ( " This is number guessing game!")
secret_number = 10

while True:
    number = int(input("Please enter a number between 1 and 10 "))
    if number == secret_number:
       print("You guessed correctly")
       break
    elif number >  secret_number:
        print("Too high. try again")
    else:
     print("Too low, try agian.")


print(list('hello'))
