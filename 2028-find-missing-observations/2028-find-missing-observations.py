class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = []
        m = len(rolls)
        roll_sum = sum(rolls)
        target = mean * (n + m) - roll_sum
        if target < n or target > 6 * n:
            return []
        
        res = [target // n] * n
        remainder = target % n

        for i in range(remainder):
            res[i] += 1
        
        return res


        


        