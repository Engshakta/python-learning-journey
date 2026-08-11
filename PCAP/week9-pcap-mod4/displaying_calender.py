import calendar
result = calendar.prmonth(2026,7)
print(result)

# Checking Leap Years (isleap(), leapdays())
print(calendar.isleap(2024))
print(calendar.leapdays(2010, 2021))
print(calendar.leapdays(2000, 2005))