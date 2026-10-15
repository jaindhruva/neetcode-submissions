class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adj matrix
        adj = defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        min_ht = float('infinity')
        res = []
        # go through each node as root
        for k in range(n):
            # and start bfs from each node
            q = deque()
            visited = set()
            q.append(k)
            ht = 0
            while q:
                size = len(q)
                for i in range(size):
                    node = q.popleft()
                    if node in visited:
                        continue
                    for nbr in adj[node]:
                        q.append(nbr)
                    visited.add(node)
                ht += 1


            if ht < min_ht:
                res = []
            min_ht = min(min_ht, ht)
            if ht == min_ht:
                res.append(k)
            
        
        return res
        
