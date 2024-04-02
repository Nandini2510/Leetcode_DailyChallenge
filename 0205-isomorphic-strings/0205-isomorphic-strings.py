class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpS = {}
        mpT = {}

        for charS, charT in zip(s,t):
            if charS in mpS:
                if mpS[charS] != charT:
                    return False
            else:
                if charT in mpT:
                    return False
                mpS[charS] = charT
                mpT[charT] = charS
        return True