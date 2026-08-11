# Comparing numeric strings lexicographically:
print("10" == "010")
print("10" > "010")
print("10" > "8")
print("20" < "8")

# Comparing strings against integers:
print("10" == 10)
print("10" != 10)
print("10" > 10) # Raises TypeError: '>' not supported between instances of 'str' and 'int'

