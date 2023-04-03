class QuickFinfUF:

    def __init__(self, n):
        self.id = [i for i in range(n)]

    def connected(self,p,q):
        return self.id[p] == self.id[q]
    
    def union(self,p,q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i]==pid:
                self.id[i] = self.id[q]


arr = QuickFinfUF(8)
