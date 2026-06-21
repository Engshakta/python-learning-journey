friends = ["Abdishakur", "Khaalid", "Aydaruus", "Siciid", "Ahmed"]

for friend in friends:
    print("Hello", friend)
print("Done")


largest_so_far = -1 
print("Before", largest_so_far)
for the_num in [-9,-41,-12,-3,-74,-10, -15]:
 if the_num > largest_so_far:
     largest_so_far = the_num
 print(largest_so_far, the_num)

print("After", largest_so_far)


count = 0
sum = 0
print( "Before", count,sum)
for things in [9,41,12,3,74, 15]:
  count =  count +1
  sum = sum + things
  print(count, sum, things) 
print( "After", count, sum, sum/count)
   

found = False
print("Before", found)

for value in [1,2,3,4,5,6,7,8,9,10]:
  if value == 3:
    found = True
  print(found, value)

print("After", found)


smallest = None 
print("Before")

for value in [1,2,3,4,5,6,7,8,9,10]:
    if smallest == None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print("After", smallest)

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')