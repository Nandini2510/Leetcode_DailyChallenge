class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans = 0, 0
        count = {}
        r = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            while count[s[r]] > 1:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
