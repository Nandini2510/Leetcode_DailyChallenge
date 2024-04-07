class Solution:
    def checkValidString(self, s: str) -> bool:
        opencount = 0
        closecount = 0
        n = len(s) -1

        for i in range(n + 1):
            if s[i] == "(" or s[i] == "*":
                opencount += 1
            else:
                opencount -= 1
            
            if s[n - i] == ")" or s[n-i] == "*":
                closecount += 1
            else:
                closecount -= 1

            if opencount < 0 or closecount < 0:
                return False
        return True