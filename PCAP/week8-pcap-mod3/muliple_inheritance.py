class Left:
    var = "L"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    def fun(self):
        return "Right"
    
class Sub(Left, Right):
    pass

obj = Sub()