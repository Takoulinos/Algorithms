import matplotlib.pyplot as plt
import math

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        plt.scatter(self.x, self.y)
        plt.show()

    def draw_to(self,p):
        x = [self.x, p.x]
        y = [self.y, p.y]
        plt.plot(x,y)
        plt.axis([0, 10, 0, 10])
        plt.show()

    def to_string(self):
        return f"({self.x}, {self.y})"
    
    def compare_to(self, p):
        if self.y < p.y or (self.y == p.y and self.x < p.x):
            return -1
        else:
            return 1
        
    def slope_to(self, p):
        if self.x == p.x:
            return math.inf
        return (p.y - self.y) / (p.x - self.x)
    
    def slope_order(self, p, q):
        if self.slope_to(p) < self.slope_to(q):
            return -1 
        return
    

# x = [3,4,5]
# y = [3,4,5]

# plt.scatter([3,4,5], [3,4,5])
# plt.axis([0, 10, 0, 10])
# plt.show()

# plt.plot(x,y)
# plt.show()