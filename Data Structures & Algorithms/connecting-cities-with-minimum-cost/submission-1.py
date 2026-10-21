class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src,dst,cost in connections:
            adj[src].append([dst, cost])
            adj[dst].append([src, cost])
        
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, [0,1])
        totalCost = 0
        while minHeap:
            cost, city = heapq.heappop(minHeap)
            if city in visited:
                continue
            totalCost += cost
            visited.add(city)
            if len(visited) == n:
                break

            for nbr,cost in adj[city]:
                if nbr in visited:
                    continue
                heapq.heappush(minHeap,[cost,nbr])
                
        return totalCost if len(visited) == n else -1
            
