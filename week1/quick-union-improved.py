class QuickUnionUF:

    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.tree_size = [1 for _ in range(n)]

    def root(self, n):
        if self.id[n] == n:
            return n
        self.id[n] = self.id[self.id[n]] #PATH COMPRESSION
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