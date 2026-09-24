class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mat = defaultdict(list)
        for u,v,t in times:
            adj_mat[u].append([v,t])
        
        min_heap = []
        visited = set()
        time = 0
        heapq.heappush(min_heap,[time,k])

        while min_heap:
            t,v = heapq.heappop(min_heap)
            if v in visited:
                continue

            visited.add(v)
            time = t
            
            if len(visited) == n:
                break
            for nbr,t2 in adj_mat[v]:
                if nbr in visited:
                    continue
                heapq.heappush(min_heap,[t2+t,nbr])

        return time if len(visited)==n else -1
