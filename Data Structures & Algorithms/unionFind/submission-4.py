class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.num_components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1

    def find(self, x: int) -> int:
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        parX = self.find(x)
        parY = self.find(y)
        if parX == parY:
            return False

        if self.rank[parX] > self.rank[parY]:
            self.par[parY] = parX
            self.rank[parX] += self.rank[parY]
        else:
            self.par[parX] = parY
            self.rank[parY] += self.rank[parX]
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        # count = 0
        # print(Counter(self.par)) 
        return self.num_components

