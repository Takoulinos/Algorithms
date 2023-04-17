import math

class ShellSort:

    def __init__(self, arr):
        self.arr = arr

    def exch(self, m, n):
        temp = self.arr[m]
        self.arr[m] = self.arr[n]
        self.arr[n] = temp

    def sort(self):
        h = 1
        while h < len(self.arr)/3:
            h = 3*h + 1
        while h >= 1:
            for i in range(h, len(self.arr), h):
                for j in range(i, i+h):
                    if j < len(self.arr) and self.arr[j] < self.arr[j - h]:
                        self.exch(j, j - h)
            h = math.floor(h/3)

arr = [9,7,5,3,1,2,4,6,8]
x = ShellSort(arr)
print(x.arr)
x.sort()
print(x.arr)