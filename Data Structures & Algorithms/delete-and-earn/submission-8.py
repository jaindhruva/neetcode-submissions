class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        sortedKeys = sorted(count.keys())

        withPrev, withoutPrev = 0, 0
        prev = None
        bestPrev = 0
        
        for n in sortedKeys:
            gain = count[n] * n
            

            if prev is not None and n == prev + 1:
                # n conflicts with prev, so taking n requires
                # the solution that did not take prev
                newWithPrev = withoutPrev + gain
            else:
                # n does not conflict with prev
                newWithPrev = bestPrev + gain

            newWithoutPrev = bestPrev
            withoutPrev = newWithoutPrev
            withPrev = newWithPrev
            bestPrev = max(withoutPrev, withPrev)
            prev = n

        return bestPrev

