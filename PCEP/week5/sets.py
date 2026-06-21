# colors = {'Blue', 'Green', 'White' , 'Red', 'Green'}
# print(colors)

my_list = [0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,10]
print(my_list)

convert_to_list = set(my_list)
print(convert_to_list)

converted_back_to_list = list(convert_to_list)

print(converted_back_to_list)

my_set = {"apple", "banana", "cherry"}

if "apple" in my_set:
    print("found")

print("Elements in the set:")
for item in my_set: 
    print(item)