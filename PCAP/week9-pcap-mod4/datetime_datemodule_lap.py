from datetime import datetime

# 1. Create the datetime object
dt = datetime(2020, 11, 4, 14, 53, 0)

# 2. Print the formatted strings
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))