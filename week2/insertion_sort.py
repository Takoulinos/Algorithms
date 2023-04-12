class InsertionSort:

    def __init__(self, arr):
        self.arr = arr

    def exch(self, m, n):
        temp = self.arr[m]
        self.arr[m] = self.arr[n]
        self.arr[n] = temp

    def sort(self):
        for i in range(1, len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j-1]:
                    self.exch(j, j-1)
                else:
                    break