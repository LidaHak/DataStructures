

    class Deque:
    def __init__(self, size=None):
        self.items = []
        self.size = size
        self.front = 0
        self.rear = 0

    def isFull(self):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            return True
        else:
            return False

    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False

    def add_first(self, item):
        self.items.append(item)

    def add_last(self, item):
        self.items.insert(0, item)

    def remove_first(self):
        return self.items.pop()

    def remove_last(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    ----------Not sure about the accuracy of this---------------------------------------------    
    def resize(self, new_size, new_value=0):
        if self.isFull():
            element_size = len(self.size[0])
            new_size = new_size * 2
            while len(self.size) <= new_size:
                n = tuple(new_value for i in range(element_size))
                self.size.append(n)
        else:
            self.size = self[:new_size]
        return self
    ---------------------------------------------------------------------------------------------

deq = Deque(10)
deq.add_first(7)
deq.add_last(9)
