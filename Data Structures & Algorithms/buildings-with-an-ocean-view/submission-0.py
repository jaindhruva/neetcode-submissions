class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            if not stack or heights[stack[-1]]<h:
                stack.append(i)
        
        stack.reverse()
        return stack