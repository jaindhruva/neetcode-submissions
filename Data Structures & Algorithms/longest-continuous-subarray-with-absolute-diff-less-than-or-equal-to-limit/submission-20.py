class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 0
        l = 0
        min_num = []
        max_num = []
        count = Counter()
        
        for r in range(n):
            heapq.heappush(min_num, nums[r])
            heapq.heappush(max_num, -nums[r])
            count[nums[r]] += 1
            while -max_num[0] - min_num[0] > limit:
                count[nums[l]] -= 1
                l += 1
                while max_num and count[-max_num[0]] == 0:
                    heapq.heappop(max_num)
                while min_num and count[min_num[0]] == 0:
                    heapq.heappop(min_num)
            res = max(res,  r - l + 1)
        
        return res
                




