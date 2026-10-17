class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        first_index = { 0: -1} # prefix_sum : starting index
        prefix_sum = 0
        longest_subarr = 0

        for i,value in enumerate(nums):
            prefix_sum += value
            needed = prefix_sum - k

            if needed in first_index:
                longest_subarr = max(longest_subarr, i - first_index[needed])
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i
        
        return longest_subarr
