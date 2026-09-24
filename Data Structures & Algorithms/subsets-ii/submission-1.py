class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        my_set = set()

        def dfs(i, curr):
            if i == n:
                if tuple(curr) not in my_set:
                    curr_copy = curr.copy()
                    res.append(curr_copy)
                    my_set.add(tuple(curr_copy))
                return
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)

        nums.sort()
        dfs(0,[])
        return res