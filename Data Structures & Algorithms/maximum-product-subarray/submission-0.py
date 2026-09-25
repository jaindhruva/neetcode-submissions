class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # for every element, track min product and product 
        # in every iteration , 
        # include the nums[i] in the calculating min and max always.
        #  we will do max(res, maxpdt in each iteratin to filter out the actual max)
        res = max_pdt = min_pdt = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            pdt = max_pdt
            max_pdt = max(n , max_pdt*n, min_pdt*n)
            min_pdt = min(n , pdt*n, min_pdt*n)

            res = max(res, max_pdt)

        return res