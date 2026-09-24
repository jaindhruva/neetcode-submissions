class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t, n = 0, len(grid)
        visited = set()
        min_heap = [[grid[0][0],0,0]]

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while min_heap:
            ele,x,y = heapq.heappop(min_heap)
            t = max(t,ele)
            if x==n-1 and y==n-1:
                break
            visited.add((x,y))
            for dir in dirs:
                x2 = x + dir[0]
                y2 = y + dir[1]
                if x2 in range(n) and y2 in range(n) and (x2,y2) not in visited:
                    heapq.heappush(min_heap,[grid[x2][y2],x2,y2])


        return t