class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        count = 0
        prefixSumIndexMap = {} # prefixSum : <list of indices with that sum>
        for i,n in enumerate(nums):
            if i == 0:
                prefix[i] = n
            else:
                prefix[i] = prefix[i-1] + n
            
            if prefix[i] == k:
                count += 1
            
            needed =  prefix[i] - k
            if needed in prefixSumIndexMap:
                count += len(prefixSumIndexMap[needed])
            
            if prefix[i] not in prefixSumIndexMap:
                prefixSumIndexMap[prefix[i]] = []
            prefixSumIndexMap[prefix[i]].append(i)
        
        return count