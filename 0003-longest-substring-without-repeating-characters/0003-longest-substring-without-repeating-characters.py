class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        count = 0
        ans = 0
        mp = {}
        
        for j in range(len(s)):
            if s[j] not in mp or mp[s[j]] < i:
                mp[s[j]] = j
                ans = max(ans, j - i + 1)
            else:
                i = mp[s[j]] + 1
                mp[s[j]]= j
        return ans