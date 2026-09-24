class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights)-1

        while l < r:
            max_water = max(max_water, (r-l)*min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
                continue
            else:
                r -= 1

        return max_water