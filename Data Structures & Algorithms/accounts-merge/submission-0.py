class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # email -> index to acc. each email has an index mapped

        # build email to index map
        for idx, act in enumerate(accounts):
            for e in act[1:]:
                if e not in emailToAcc:
                    emailToAcc[e] = idx
                else:
                    uf.union(idx, emailToAcc[e]) 
                    # this email already has been mapped, 
                    # means it must be connected to possibly other emails. 
                    # so join(union) this with old index.
                
        emailGroup = defaultdict(list) # index of acc -> list of emails
        # build map of leader of an email group/set -> list of emails in that set
        for e,i in emailToAcc.items(): 
            # go through each email and find its leader and 
            # add that email to the leader
            leader = uf.find(i) # finds the parent of this email
            emailGroup[leader].append(e) # append to leader
        
        res = []
        for i,emails in emailGroup.items():
            name = accounts[i][0] # first item is name in original list
            res.append([name]+emailGroup[i])
        return res


        








