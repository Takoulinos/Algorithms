class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def peek(self):
        return self.first

    def enqueue(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        if self.size == 1:
            self.last = None
        temp = self.first.value
        self.first = self.first.next
        self.size -= 1
        return temp
    
    def is_empty(self):
        return self.size == 0