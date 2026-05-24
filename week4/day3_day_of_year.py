# def is_year_leap(year):

#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
    
# def days_in_month (year, month):
#     if month < 1 or month > 12:
#         return None
    
#     days = [31, 28, 31, 30, 31, 30,
#         31, 31, 30, 31, 30, 31]

#     if month == 2 and is_year_leap(year):
#         return 29
#     return days[month -1]

# def day_of_year(year, month, day):
#     if month < 1 or month > 12:
#         return None
#     days = days_in_month(year, month)
    
#     if day < 1 or day > days:
#         return None
    
#     total_days = day
#     for m in range(1, month):
#         total_days += days_in_month(year, m)
    
#     return total_days

# print(day_of_year(2000, 12, 31))
# print(day_of_year(2024, 2, 29))
# print(day_of_year(2023, 2, 29))
# print(day_of_year(2025, 1, 1))
# print(day_of_year(2025, 13, 1))
# print(day_of_year(2025, 4, 31))


# def scope_test():
#     x = 123

# scope_test ()

# print(x)

# def my_function():
#     var = 2
#     print("Do i know that variable", var)
# var = 1

# my_function()

# print(var)

# x = 10

# def test():
#   number = 4
  
#   return number + 5

# print(test())
  

# visits = 0
# def add_visit():
#     global visits
#     return visits + 1

# print(add_visit())

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)

# var = 1

# my_function(var)
# print(var)
    
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)



