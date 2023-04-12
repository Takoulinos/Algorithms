class SelectionSort:

    def __init__(self, arr):
        self.arr = arr

    def exch(self, m, n):
        temp = self.arr[m]
        self.arr[m] = self.arr[n]
        self.arr[n] = temp

    def sort(self):
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.exch(i, min_index)