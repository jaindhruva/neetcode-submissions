class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0]*10001
        for n in nums:
            points[n] += n
        prev = best = 0
        for score in points:
            prev, best = best, max(best, prev+score)

        return best

