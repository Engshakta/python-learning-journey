
my_list = [1,2,3,4,5,6,7,8,9,10]
to_find = 55

found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find

    if found:
        break

if found :
    print("Element found at index ", i)
else:
    print("absent")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("The list with unique elements only: ")
print(unique_list)


i =2 
while i >= 0:
    print("*")
    i -=2

for i in range(-1,1):
    print("#")

z= 10
y = 0
x = z > y or z == y

print(x)

my_list = [3,1,-1]
my_list[-1] = my_list[-2]
print(my_list)

vals = [0,1,2]
vals[0],vals[1] = vals[1], vals[0]

print(vals)

nums = []
valss = nums[:]
valss.append(1)
print(valss)
print(nums)

my_lis = [0 for i in range (1,3)]
print(my_lis)

my_listed = [0,1,2,3]
x = 1
for elem in my_listed:
    x *= elem
print(x)

var = [ 0,1,2]
var.insert(0,1)
print(var)
# del var[1]
print(var) 
# result is 4

x = 1
x = x == x
print(x)

new_list = [3,1,-2]
print(new_list[new_list[-1]])

i = 0
while i <= 3:
    i +=2
    print("*")
mylist= [i for i in range(-1,2)]
print(mylist)

far = 1
while far < 10:
    print("#")
    far = far << 1

array = [1,2,3,4]
print(array[-3:-2])

for i in range(1):
    print("#")
else:
    print("#")

nms = [1,2,3]
vls = nms[-1:-2]

print(nms)
print(vls)


i = 0
while i <=5:
    i +=1
    if i%2 ==0:
        break
    print("*")

lst = [1,2,3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
    print(lst)

car = 0
while car < 6:
    car +=1
    if car % 2 == 0:
        continue
    print("#")
    

z = 10
y = 0
z = y<z and z > y or y>z and z<y
print(x)

nms = [1,2,3]
vals = nms
del vals[1:2]
print(nms)
print(vals)

# my_list = [[0,1,2,3] for i in range(2) ]
# print(my_list[2][0])
# # the snippest will cause run time error

# vals = [0,1,2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)



a =1
b =0
c = a & b
d = a | b
e = a ^ b

print(c+d+e)
