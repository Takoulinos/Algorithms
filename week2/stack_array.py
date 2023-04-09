class Stack:

    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def peek(self):
        return(self.array[len(self.array - 1)])
    
    def pop(self):
        return self.array.pop()

    def is_empty(self):
        if not self.array:
            return True
        return False