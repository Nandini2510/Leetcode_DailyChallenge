class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = {0:0, 1:1, 6:9, 8:8, 9:6}
        res = 0
        num = n
        while n > 0:
            x = n % 10
            if x not in s:
                return False
            res = res * 10 + s[x]
            n //= 10
        return res != num
        