class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)

        q = deque()
        visit = set()
        n = len(edges)+1

        # add leaves to q
        for node in adj.keys():
            if len(adj[node]) == 1:
                q.append(node)


        count = 0
        layers = 0
        while count <  n-2:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                for nbr in adj[node]:
                    adj[nbr].remove(node)
                    break
                adj.pop(node)
                count += 1
            layers += 1

            for node in adj.keys():
                if len(adj[node]) == 1:
                    q.append(node)

        print(count, layers)
        if count == n-1:
            return 2*layers
        else:
            return 1+2*layers