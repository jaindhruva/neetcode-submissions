class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_score = 0
        best_left = values[0]
        for j in range(1,n):
            max_score = max(max_score, best_left + values[j] - j)
            best_left = max(best_left, values[j] + j)

        return max_score