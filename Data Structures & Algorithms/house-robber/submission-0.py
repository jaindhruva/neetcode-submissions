class Solution:
    def rob(self, nums: List[int]) -> int:
        with_prev, without_prev = 0,0

        for n in nums:
            max_so_far = max(with_prev, n+without_prev)
            without_prev = with_prev
            with_prev = max_so_far
        
        return with_prev