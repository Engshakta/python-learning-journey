try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1 / value)
except ValueError:
    print("I don\'t know what to do")
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe')
except :
    print('Something went wrong!')

name = input("Enter your name")

password = input(" please enter your password: ")




result = f"your name is {name} and your password is {password}"
print(result)
          
print(
"""
Dear User, 
welcome to Python programming 
This  messsage is brought ro you by own code. 

Thanks,
The Python team
"""
)

print("Name:\tAlice\nAge:\t30\nStatus:\tActive")