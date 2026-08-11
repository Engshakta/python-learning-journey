import calendar

# print(calendar.calendar(2026))

# result = calendar.weekday(2026, 7, 20)
# print(result)


# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.weekheader(1))

# c = calendar.Calendar()
# for val in c.itermonthdays(2026, 8):
#     print(val, end = " ")

# c = calendar.Calendar(calendar.SUNDAY)

# for val in c.itermonthdays(2019, 11):
#     print(val, end = " ")



c = calendar.Calendar(calendar.MONDAY)
zeros_counter = 0

for val in c.itermonthdays(2019, 11):
    if val == 0:
        zeros_counter += 1

print(zeros_counter)