import calendar
c = calendar.Calendar()

weeks = c.monthdays2calendar(2019,11)

for week in weeks:
    print(week)