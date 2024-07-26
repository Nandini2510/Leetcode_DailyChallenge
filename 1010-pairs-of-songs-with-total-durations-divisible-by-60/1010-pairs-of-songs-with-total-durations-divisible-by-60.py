class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for t in time:
            if t % 60 == 0:
                res += mp[0]
            else:
                res += mp[60 - t % 60]
            mp[t % 60] += 1
        return res 
