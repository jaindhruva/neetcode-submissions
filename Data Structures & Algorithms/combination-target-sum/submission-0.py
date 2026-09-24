class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(curr, i, sum):
            if sum == target:
                res.append(curr.copy())
                return
            if i >= n or sum>target:
                return
            num = nums[i]
            curr.append(num)
            dfs(curr, i, sum+num)
            curr.pop()
            dfs(curr, i+1, sum)    

        dfs([], 0, 0)
        
        return res