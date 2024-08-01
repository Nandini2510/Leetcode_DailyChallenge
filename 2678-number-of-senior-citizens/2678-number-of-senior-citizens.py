class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            tempAge = detail[11] + detail[12]
            age = int(tempAge)
            if age > 60:
                res += 1
        return res
        