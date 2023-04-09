import random

class RandomizedQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, value):
        self.items += [value]

    def dequeue(self):
        r = random.randint(0, len(self.items) - 1)
        temp = self.items[r]
        self.items[r] = self.items[len(self.items) - 1]
        self.items[len(self.items) - 1] = temp
        return self.items.pop()
    
    def sample(self):
        r = random.randint(0, len(self.items) - 1)
        return self.items[r]
