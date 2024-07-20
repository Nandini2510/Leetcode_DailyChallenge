class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        numDistinct = 0
        mp = defaultdict(int)
        l, r = 0, 0
        res = 0

        while r < len(s):
            if mp[s[r]] == 0:
                numDistinct += 1
            mp[s[r]] += 1
            while numDistinct > k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    numDistinct -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            
            

        