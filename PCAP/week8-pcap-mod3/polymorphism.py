class One:
    def do_it(self):
        print("do_it from One")
    
    def doanything(self):
        self.do_it()
class Two(One):
    def do_it(self):
        print("do_it from Two")

class Three(Two):
    pass

one = One()
two = Two()
three = Three()

one.doanything()
two.doanything()
three.doanything()