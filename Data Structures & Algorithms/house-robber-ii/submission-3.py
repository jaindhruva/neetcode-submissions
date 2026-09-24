class Solution:
    def rob(self, nums: List[int]) -> int:
        with_prev, without_prev = 0, 0
        with_prev2, without_prev2 = 0, 0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-1):
            n = nums[i]
            max_so_far = max(with_prev, without_prev + n)
            without_prev = with_prev
            with_prev = max_so_far

            n = nums[i+1]
            max_so_far2 = max(with_prev2, without_prev2 + n)
            without_prev2 = with_prev2
            with_prev2 = max_so_far2
        

        return max(with_prev, with_prev2)