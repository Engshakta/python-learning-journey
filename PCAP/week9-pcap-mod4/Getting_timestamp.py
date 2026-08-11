from datetime import datetime
dt = datetime(2020, 10, 4, 14, 55)
seconds = dt.timestamp()
print(seconds)

from datetime import datetime

# Set it to a safe, modern year
my_dt = datetime(2026, 7, 15, 12, 0, 0)
print(type(my_dt.timestamp()))