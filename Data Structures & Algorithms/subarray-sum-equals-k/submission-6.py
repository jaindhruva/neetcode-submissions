class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        count = 0
        prefixSumCountMap = defaultdict(int) # prefixSum : count of indices with that sum
        for i,n in enumerate(nums):
            if i == 0:
                prefix[i] = n
            else:
                prefix[i] = prefix[i-1] + n
            
            if prefix[i] == k:
                count += 1
            
            needed =  prefix[i] - k
            count += prefixSumCountMap[needed]
            prefixSumCountMap[prefix[i]] += 1
        
        return count