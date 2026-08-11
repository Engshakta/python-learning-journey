from datetime import date, time
user_birthday = date(2025, 2, 9)
print(user_birthday)

# Feeding a manual number of seconds into the converter

t = time(8,51,49)
print(t)

# handles optional settings on this pocket watch
mystery_time = time(minute = 30)
print(mystery_time)

# count down message timer

import time                       # This keeps the 'time' module named 'time'
from datetime import time as dt_time  # This renames the class to 'dt_time'!
print("Ready...")
time.sleep(1)
print("Go!")

print(time.ctime())
luncth_time = dt_time(12, 30)

# writing time in string format


d = date(2026, 7, 14)  # Correct order: Year 2026, Month 7, Day 14
print(d.strftime("%Y/%m/%d"))



from datetime import datetime  as dt
event_log = dt(2026, 7, 14)
print(event_log)