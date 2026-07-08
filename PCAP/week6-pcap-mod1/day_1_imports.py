# # The first way to import a module
# import math

# result =  math.sin(math.pi / 2)
# print(f"The calculation result is: {result}")

# #how the two namespaces (yours and the module's one) can coexist.
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None

# pi = 3.14

# print(sin(pi / 2))
# print(math.sin(math.pi / 2))


# # the second way to import module is The Mechanics of Selective Imports
# from math import sin, pi # you can only use this two!
# print(sin(pi / 2)) # No dot notaion required

# # it has also name collison effect


# from math import pi

# # You define a local variable with the exact same name
# pi = "Data Center" 

# print(pi)  
# #  Outputs: Data Center
# #  The mathematical constant value (3.14159...) has been completely overwritten and lost


pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))

from math import sin, pi
print(sin(pi / 2))