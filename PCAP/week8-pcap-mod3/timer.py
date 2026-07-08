class Timer:
    def __init__(self, hours = 0, minitues = 0, seconds = 0):
        self.__hours = hours
        self.__minitues = minitues
        self.__seconds = seconds
    
    def __str__(self):
        return f"{ self.__hours:02d} : {self.__minitues:02d} : {self.__seconds:02d}"
    
    def next_seconds(self):
        self.__seconds +=1

        if self.__seconds== 60:
            self.__seconds= 0
            self.__minitues +=1

            if self.__minitues == 60:
                self.__minitues = 0
                self.__hours += 1

                if self.__hours == 24:
                    self.__hours = 0
    def prev_seconds(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minitues -= 1

            if self.__minitues == -1:
                self.__minitues = 59
                self.__hours -= 1

                if self.__hours == -1:
                    self.__hours = 23
              

timer = Timer(0 , 0 , 0)
print("Midnight: ", timer)

timer.prev_seconds()
print("Tick Backwards:", timer)

timer.next_seconds()
print("Tick Forward:", timer)