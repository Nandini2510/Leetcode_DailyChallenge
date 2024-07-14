class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        res = []
        while i < j:
            sumTarget = numbers[i] + numbers[j]
            if sumTarget == target:
                res.append(i + 1)
                res.append(j + 1)
                break
            elif sumTarget > target:
                j -= 1
            else:
                i += 1
        return res
