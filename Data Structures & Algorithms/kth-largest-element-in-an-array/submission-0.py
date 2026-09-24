class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [ -n for n in nums]
        min_heap = []
        for n in nums:
            min_heap.append(n)
        heapq.heapify(min_heap)

        res = -1
        for i in range(k):
            res = heapq.heappop(min_heap)
        return -res