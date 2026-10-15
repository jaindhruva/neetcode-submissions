class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for n in arr:
            heapq.heappush(min_heap, (abs(n-x), n))

        res = []
        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        res.sort()
        return res