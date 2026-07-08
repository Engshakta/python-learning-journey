# from random import random , seed 
# seed(0)
# for i in range(5):
#     print(random())

# import random

# # We hardcode the "page" to 7
# random.seed(7)

# print(random.random())
# print(random.random())

# import random

# random.seed(7)  # Set the path

# # Ask for a whole number between 1 and 10
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))

from random import choice

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))  # Outputs just ONE item, like: 4

from random import sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Give me 5 unique numbers
print(sample(my_list, 5))   # Outputs a list of 5 items: [3, 1, 8, 9, 10]

# 2. Give me 10 unique numbers (the whole bag!)
print(sample(my_list, 10))  # Outputs all 10 items perfectly shuffled: [10, 8, 5, 1, 6, 4, 3, 9, 7, 2]