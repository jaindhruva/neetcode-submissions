class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = []
        visited = set()
        total_cost, n = 0, len(points)

        heapq.heappush(min_heap,[0,0])

        while min_heap:
            cost,node = heapq.heappop(min_heap)
            if node in visited:
                continue
            total_cost += cost
            visited.add(node)
            # if len(visited) == n:
            #     break
            for i in range(n):
                if i in visited:
                    continue
                x1,y1 = points[node][0], points[node][1]
                x2,y2 = points[i][0], points[i][1]
                man_dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(min_heap, [man_dist, i])
        
        return total_cost
