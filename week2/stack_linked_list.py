class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def peek(self):
        return self.top
    
    def push(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.top = newNode
        else:
            temp = self.top
            self.top = newNode
            newNode.next = temp
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        self.top = self.top.next
        self.size -= 1

    def is_empty(self):
        return self.size == 0