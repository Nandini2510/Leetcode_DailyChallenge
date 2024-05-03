class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        s = set()
        for i in range(len(nums)):
            if nums[i] < 0:
                s.add(nums[i])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                if -1 * nums[i] in s:
                    res = max(res, nums[i])
        return res
