class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res_copy = res.copy()
            for subset in res_copy:
                new_subset = subset + [num]
                res.append(new_subset)
            # res += [subset + [num] for subset in res]

        return res

        # for num in nums:
        #     res_copy = res.copy()

        #     for subset in res_copy:
        #         new_subset = subset + [num]
        #         res.append(new_subset)