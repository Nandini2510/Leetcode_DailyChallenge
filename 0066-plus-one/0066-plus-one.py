class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        num = ""

        for digit in digits:
            num += str(digit)
        
        num = str(int(num) + 1)
        for c in num:
            res.append(int(c))

        return res
            

        