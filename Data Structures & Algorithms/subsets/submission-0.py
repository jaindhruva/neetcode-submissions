class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            # res_copy = res.copy()
            # for subset in res_copy:
            #     subset.append(n)
            #     res = res + subset
            res += [subset + [num] for subset in res]

        return res