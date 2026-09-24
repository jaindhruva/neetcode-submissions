class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        n = len(nums)


        def dfs(perm):
            if len(perm) == n:
                res.append(perm.copy())
            for i in range(n):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    perm.append(nums[i])
                    dfs(perm)
                    perm.pop()
                    visited.remove(nums[i])

        dfs([])


        return res