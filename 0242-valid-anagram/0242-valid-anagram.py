class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = defaultdict(int)

        for ch in range(len(s)):
            anagram[s[ch]] += 1
        
        for ch in range(len(t)):
            anagram[t[ch]] -= 1
        
        for k, v in anagram.items():
            if (anagram[k] > 0 or anagram[k] < 0 ):
                return False
        return True
        