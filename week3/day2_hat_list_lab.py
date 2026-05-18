hat_list = [1, 2, 3, 4, 5]

number = int(input("Enter a number to replace the middle number: "))

hat_list[2] = number

del hat_list[4]

print(len(hat_list))

print(hat_list)