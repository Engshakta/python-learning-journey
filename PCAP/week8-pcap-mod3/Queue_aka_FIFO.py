class QueueError(IndexError):
    pass
class Queue:
    def __init__(self):
        self.queue = []
    
    def put(self, element):
        self.queue.insert(0, element)
    
    def get(self):
        if len(self.queue) == 0:
            raise QueueError
        element = self.queue[-1]
        del self.queue[-1]
        return element

class SuperQueue(Queue):
    def isempyt(self):
        return len(self.queue) == 0
