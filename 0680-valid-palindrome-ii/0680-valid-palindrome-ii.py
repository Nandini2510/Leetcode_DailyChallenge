class Solution:
    def validPalindrome(self, s: str) -> bool:
        c = 1
        i, j = 0, len(s) - 1

        def isPalindrome(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        

        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i + 1, j, s) or isPalindrome(i , j - 1, s)
            i += 1
            j -= 1
        return True


