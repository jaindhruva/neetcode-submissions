class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = [] # monotonically decreasing stack
        n = len(heights)
        res = [0]*n
        for i in range(n-1,-1,-1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                res[i] += 1
            if stack:
                res[i] += 1
            stack.append(heights[i])

        return res
            