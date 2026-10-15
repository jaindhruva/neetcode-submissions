class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adj matrix
        adj = defaultdict(list)
        degree = [0]*n
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            degree[src] += 1
            degree[dst] += 1

        leaves = deque()
        for i, deg in enumerate(degree):
            if deg == 1:
                leaves.append(i)
        
        remaining = n
        res = []
        while remaining >2:
            size = len(leaves)
            remaining -= size
            for i in range(size):
                node = leaves.popleft()
                for nbr in adj[node]:
                    degree[nbr] -= 1
                    if degree[nbr] == 1:
                        leaves.append(nbr)
                
        
        return list(leaves) if n>1 else [0]
        
