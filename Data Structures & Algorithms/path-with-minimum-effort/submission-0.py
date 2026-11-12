class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        min_heap = [] # (abs diff, x, y)
        heapq.heappush(min_heap, (0,0,0))
        max_diff = 0
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        while min_heap:
            abs_diff, x, y = heapq.heappop(min_heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            max_diff = max(max_diff, abs_diff)
            if x == m-1 and y == n-1:
                break
            
            for dx,dy in dirs:
                i = x + dx
                j = y + dy

                if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
                    continue
                heapq.heappush(min_heap, (abs(heights[i][j]-heights[x][y]), i, j) )

        return max_diff