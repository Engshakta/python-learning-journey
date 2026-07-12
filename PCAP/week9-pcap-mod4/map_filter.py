numbers = [10,15,20,25]
transformed = list(map(lambda x : x + 10, numbers))
print(transformed)

numbers = [10,15,20,25]
filtered_output = list(filter(lambda x : x > 20, numbers))
print(filtered_output)

numbers = [1,2,3,4]
odds = filter(lambda x : x % 2 != 0, numbers)
result = list(map(lambda x : x * 10, odds))
print(result)