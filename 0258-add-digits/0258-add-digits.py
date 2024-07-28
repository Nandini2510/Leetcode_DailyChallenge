class Solution:
    def addDigits(self, num: int) -> int:
        

        while num > 9:
            res = 0
            while num != 0:
                num, m = divmod(num, 10)
                res += m
            num = res

        return num
        