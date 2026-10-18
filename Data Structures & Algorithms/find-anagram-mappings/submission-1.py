class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2_map = {}
        for i,n2 in enumerate(nums2):
            n2_map[n2] = i
        
        res = []
        for n1 in nums1:
            res.append(n2_map[n1])

        return res
