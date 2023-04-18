#  implementation of a priority queue using binary heap data structure

class MaxPriorityQueue:

    def __init__(self):
        self.pq = [None]
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def insert(self, item):
        self.pq.append(item)
        self.size += 1
        self.swim(self.size)

    def delete_max(self):
        self.exchange(1, self.size)
        value = self.pq.pop()
        self.size -= 1
        self.sink(1)
        return value
    
    def swim(self, k):
        while k > 1 and self.pq[int(k/2)] < self.pq[k]:
            self.exchange(k, int(k/2))
            k = int(k/2)
            
    def sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if j < self.size and self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[k] >= self.pq[j]:
                break
            self.exchange(k,j)
            k = j
        
    def exchange(self, m, n):
        self.pq[m], self.pq[n] = self.pq[n], self.pq[m]