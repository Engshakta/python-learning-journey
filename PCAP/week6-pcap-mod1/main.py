# import module
# print(module.counter)
from sys import path
 
path.append('..∖∖modules')
 
import module
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

