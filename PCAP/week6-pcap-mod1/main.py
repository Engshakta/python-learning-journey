# import module
# print(module.counter)
from sys import path

 # Append custom directory to the end of Python's search list
path.append('..∖∖modules') # Using relative path with doubled backslashes for Windows

 
import module
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

