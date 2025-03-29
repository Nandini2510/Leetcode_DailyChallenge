class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = Counter()

        left = right = 0
        res = 0

        while right < len(s):
            r = s[right]
            mp[r] += 1

            while mp[r] > 1:
                l = s[left]
                mp[l] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res

