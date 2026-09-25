class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [(amount+1)] * (amount+1)
        dp[0] = 0

        for c in coins:
            sum = 0
            while sum <= amount:
                if sum - c >= 0:
                    dp[sum] = min(dp[sum],1+dp[sum-c])
                sum += 1


        return -1 if dp[amount] == amount+1 else dp[amount]