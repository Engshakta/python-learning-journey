class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class CountingStacks(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0
    
    def get_counter(self):
        return self.__counter
    
    def pop(self):
        val = Stack.pop(self)
        self.__counter += 1
        return val