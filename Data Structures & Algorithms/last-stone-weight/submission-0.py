class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            diff = stone1 - stone2
            if diff == 0:
                continue
            heapq.heappush(stones, diff)
        
        return 0 if len(stones) == 0 else -stones[0]