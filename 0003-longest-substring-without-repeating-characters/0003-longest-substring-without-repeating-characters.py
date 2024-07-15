class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = defaultdict(int)
        l =  0

        for r in range(len(s)):
            if s[r] not in mp or mp[s[r]] < l:
                mp[s[r]] = r
                res = max(res, r - l + 1)
            else:
                l = mp[s[r]] + 1
                mp[s[r]] = r
        return res



        