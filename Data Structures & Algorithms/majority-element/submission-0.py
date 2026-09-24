class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        maj_elem, max_count = None, 0
        for n in nums:
            count_map[n] += 1
            if count_map[n] > max_count:
                maj_elem = n
                max_count = count_map[n]
        
        return maj_elem
        