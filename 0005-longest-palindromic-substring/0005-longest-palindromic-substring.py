class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) == 0:
            return ""
        
        longest = ""
        for i in range(len(s)):
            odd_palindrome = checkPalindrome(s, i, i)
            even_palindrome = checkPalindrome(s, i, i+1)
            longest = max(longest,odd_palindrome, even_palindrome, key=len)
        return longest