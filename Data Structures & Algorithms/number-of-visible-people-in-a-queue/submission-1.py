class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n
        
        for i in range(n-1):
            max_so_far = 0
            for j in range(i+1, n):
                max_so_far = max(max_so_far, heights[j])
                if heights[j] == max_so_far:
                    res[i] += 1
                if heights[j] >= heights[i]:
                    break
        return res

