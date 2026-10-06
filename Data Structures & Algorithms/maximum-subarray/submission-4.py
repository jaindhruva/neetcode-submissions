class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*2 for i in range(n)]
        dp[0][0] = dp[0][1] = nums[0]
        res = max(dp[0][0], dp[0][1])
        for i in range(1,n):
            dp[i][0] = nums[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + nums[i]
            res = max(res, dp[i][0], dp[i][1])
        
        return res
