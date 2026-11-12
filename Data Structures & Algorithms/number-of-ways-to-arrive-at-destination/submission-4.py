class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        min_heap = []
        adj = [[] for _ in range(n)]

        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        
        dist = [float("inf")] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        heapq.heappush(min_heap,(0,0))
        while min_heap:
            curr_dist,u = heapq.heappop(min_heap)
            if curr_dist > dist[u]:
                continue

            for v, time in adj[u]:
                new_dist = curr_dist + time

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(min_heap,(new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n - 1]

