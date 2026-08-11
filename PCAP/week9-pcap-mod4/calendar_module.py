import calendar
class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        counter = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year,month):
                for day, day_of_week in week:
                    if day != 0 and day_of_week == weekday:
                        counter += 1
        return counter

   

my_cal = MyCalendar()
print(my_cal.count_weekday_in_year(2019,0))