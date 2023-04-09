class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Deque:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.first.previous = new_node
            temp = self.first
            self.first = new_node
            self.first.next = temp
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            temp = self.last
            self.last = new_node
            self.last.previous = temp
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return
        node = self.first
        self.first = self.first.next
        self.first.previous = None
        self.size -= 1
        return node.value

    def remove_last(self):
        if self.is_empty():
            return
        node = self.last
        self.last = self.last.previous
        self.last.next = None
        self.size -= 1
        return node.value