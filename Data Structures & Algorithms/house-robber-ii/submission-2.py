class Solution:
    def rob(self, nums: List[int]) -> int:
        with_prev, without_prev = 0, 0

        if len(nums) == 1:
            return nums[0]

        for n in nums[:len(nums)-1]:
            max_so_far = max(with_prev, without_prev + n)
            without_prev = with_prev
            with_prev = max_so_far
        
        max1 = with_prev
        with_prev, without_prev = 0, 0

        for n in nums[1:]:
            max_so_far = max(with_prev, without_prev + n)
            without_prev = with_prev
            with_prev = max_so_far
        max2 = with_prev

        return max(max1, max2)