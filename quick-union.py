class QuickUnionUF:

    def __init__(self, n):
        self.id = [i for i in range(n)]

    def root(self, n):
        if self.id[n] == n:
            return n
        return self.root(self.id[n])
    
    def find(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        self.id[self.root(p)] = self.id[self.root(q)]   