class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        for ch in s:
            if ch.isalnum():
                res += ch.lower()
        print(res)
        i, j = 0, len(res) - 1
        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True
