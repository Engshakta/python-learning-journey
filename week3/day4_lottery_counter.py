drawn = [5,11,9,42,3,49]
bets = [3,7,11,42,34,49]

hits = 0

for numbers in bets:
    if numbers in drawn:
        hits += 1
print(hits)

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