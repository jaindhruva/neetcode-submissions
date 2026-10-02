class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l, r = 0, 0
        subArrSum = 0
        while r < len(arr):
            if r-l+1 > k:
                subArrSum -= arr[l]
                l += 1
            subArrSum += arr[r]
            if r-l+1 == k:
                if subArrSum // k >= threshold:
                    count += 1
            r += 1
        
        return count


