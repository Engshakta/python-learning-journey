class WeekDayError(Exception):
    pass

class Weeker:
    __valid_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.__valid_days:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day
    
    def add_days(self, n):
        current_index = Weeker.__valid_days.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = Weeker.__valid_days[new_index]
    
    # Fixed the spelling from 'substract_days' to 'subtract_days'
    def subtract_days(self, n):
        current_index = Weeker.__valid_days.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = Weeker.__valid_days[new_index]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)  
    print(weekday)
    
    # --- ADD THIS LINE TO TRIGGER THE EXCEPTION ---
    weekday_error = Weeker('Banana')

except WeekDayError:
    print("Sorry, I can't serve your request.")