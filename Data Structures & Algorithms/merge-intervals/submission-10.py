class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 1
        intervals.sort()
        res.append(intervals[0])
        resi = 1
        # if len(intervals) == 1:
        #     return intervals
        
        while i < len(intervals):
            # no overlap
            while i < len(intervals) and intervals[i][0] > res[resi-1][1]:
                res.append(intervals[i])
                i += 1
                resi += 1
                continue

            # found overlap
            while i < len(intervals) and intervals[i][0] <= res[resi-1][1]:
                res[resi-1][0] = min(intervals[i][0], res[resi-1][0])
                res[resi-1][1] = max(intervals[i][1], res[resi-1][1])
                i += 1

        
        
        return res
            
            
