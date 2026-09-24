class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            hashset.add(n)
        
        max_count = 0

        for n in nums:
            if n not in hashset:
                continue
            
            while n-1 in hashset:
                n = n-1
            
            start = n
            count = 0
            while n in hashset :
                count += 1
                hashset.remove(n)
                n = n+1
            max_count = max(max_count, count)
        
        return max_count
            
