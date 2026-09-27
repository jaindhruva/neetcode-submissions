class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        while i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] >= newInterval[0]:    
                break
            res.append(interval)
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            interval = intervals[i]
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res