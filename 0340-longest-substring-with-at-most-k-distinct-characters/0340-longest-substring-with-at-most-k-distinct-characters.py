class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = {}
        i = 0

        for j , l in enumerate(s):
            count[l] = count.get(l, 0) + 1
            if len(count) > k:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
        return j - i + 1