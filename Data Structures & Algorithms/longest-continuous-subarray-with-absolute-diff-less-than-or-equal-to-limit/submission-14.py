class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 1

        for i in range(n):
            max_n = min_n = nums[i]
            for j in range(i+1, n):
                min_n = min(min_n, nums[j])
                max_n = max(max_n, nums[j])
                if max_n - min_n > limit:
                    break
                res = max(res, j-i+1)

        return res