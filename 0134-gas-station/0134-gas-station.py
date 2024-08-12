class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        res = 0
        if sum(gas) < sum(cost):
            return -1
        diff = [0 for _ in range(len(gas))]

        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        
        for i in range(len(gas)):
            total += diff[i]
            if total < 0:
                total = 0
                res = i + 1
        return res
            
