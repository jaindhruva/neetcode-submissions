class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: p[1])
        answer = 1
        end = points[0][1]

        for left, right in points:
            if left > end:
                answer += 1
                end = right
        
        return answer
