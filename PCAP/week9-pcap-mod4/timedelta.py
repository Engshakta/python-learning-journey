from datetime import date
birthday_this_year = date(2026, 11, 4)
birthday_next_year = date(2027, 11, 4)

difference = birthday_next_year - birthday_this_year

print(type(difference))
print(difference)

from datetime import date, timedelta

today = date(2026, 7, 19)
ten_days = timedelta(days=10)

result = today + ten_days
print(result)


from datetime import timedelta
two_weeks = timedelta(weeks = 2)
print(two_weeks.days)

from datetime import datetime, timedelta

start_str = "2026/07/19"
duration = timedelta(days=2)

# Line A
dt_start = datetime.strptime(start_str, "%Y/%m/%d")

# Line B
final_moment = dt_start + duration

print(type(final_moment))