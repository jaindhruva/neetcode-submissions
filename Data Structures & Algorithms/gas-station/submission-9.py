class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        res = 0
        
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(n):
            total += gas[i]-cost[i]

            if total < 0:
                total = 0
                res = i+1

        return res
