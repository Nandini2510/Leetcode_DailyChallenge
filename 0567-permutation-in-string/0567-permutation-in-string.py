class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for char in s1:
            s1_count[char] += 1
        
        for i in range(len(s1)):
            s2_count[s2[i]] += 1
        
        matches = 0
        for char in s1_count:
            if s1_count[char] == s2_count[char]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1_count):
                return True
            char = s2[r]
            s2_count[char] += 1
            if char in s1_count:
                if s1_count[char] == s2_count[char]:
                    matches += 1
                elif s1_count[char] + 1 == s2_count[char]:
                    matches -= 1
            char = s2[l]
            s2_count[char] -= 1
            if char in s1_count:
                if s1_count[char] == s2_count[char]:
                    matches += 1
                elif s1_count[char] - 1 == s2_count[char]:
                    matches -= 1
            l += 1
        return matches == len(s1_count)