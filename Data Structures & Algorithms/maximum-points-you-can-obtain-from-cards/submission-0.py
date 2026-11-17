class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_sum = 0
        for i in range(k):
            curr_sum += cardPoints[i]

        max_score = curr_sum   
        l, r = len(cardPoints)-1, k-1
        while r >= 0:
            curr_sum -= cardPoints[r]
            r -= 1
            curr_sum += cardPoints[l]
            l -= 1
            max_score = max(max_score, curr_sum)
        
        return max_score
