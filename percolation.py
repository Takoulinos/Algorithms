from percolation_stats import Percolation_Stats

class Percolation:

    def __init__(self, n):
        self.id = [None for i in range(n*n + 2)]
        self.id[0] = 0
        self.id[n*n + 1] = n*n + 1
        self.tree_size = [1 for i in range(n*n + 2)]
        self.no_open = 0
        self.n = n
    
    def root(self, n):
        if self.id[n] == n:
            return n
        return self.root(self.id[n])
    
    def find(self, p, q):
        return self.root(p) == self.root(q)
        
    def union(self, p, q):
        if p == q:
            return
        i = self.root(p)
        j = self.root(q)
        if self.tree_size[i] < self.tree_size[j]:
            self.id[i] = self.id[j]
            self.tree_size[j] += self.tree_size[i]
        else:
            self.id[j] = self.id[i]
            self.tree_size[i] += self.tree_size[j]

    def open(self, p):
        if self.is_open(p):
            return
        self.id[p] = p
        self.no_open += 1

        if p <= self.n:
            self.union(p, 0)
        
        if p >= self.n**2 - self.n:
            self.union(p, self.n**2 + 1)

        if p < self.n**2 - self.n:
            if self.is_open(p + self.n):
                self.union(p, p + self.n)

        if p > self.n:
            if self.is_open(p - self.n):
                self.union(p, p - self.n)

        if p % self.n != 0:
            if self.is_open(p + 1):
                self.union(p, p + 1)

        if p % self.n != 1:
            if self.is_open(p - 1):
                self.union(p, p - 1)

    def is_open(self, p):
        if self.id[p]:
            return True
        return False

    def is_full(self, p):
        if not self.id[p]:
            return True
        return False

    def number_of_open_sites(self):
        return self.no_open

    def percolates(self):
        return self.find(0, self.n**2 + 1)
    
    