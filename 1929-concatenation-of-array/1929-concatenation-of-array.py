class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        length_res = 2*n
        res = [0] * length_res
        print(res)
        for i in range(n):
            res[i] = nums[i]
            res[i+n] = nums[i]
        return res