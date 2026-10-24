class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        minHeap = []
        for i in range(n-1):
            climb = heights[i+1]-heights[i]
            if climb <= 0:
                continue
            heapq.heappush(minHeap, climb)
            if len(minHeap)>ladders:
                bricks -= heapq.heappop(minHeap)
            if bricks<0:
                return i
        return n-1
