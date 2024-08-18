class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        cache = {}

        def dfs(i, target):
            if (i, target) in cache:
                return cache[(i, target)]
            if i >= len(nums) or target < 0:
                return False
            if target == 0:
                return True
            if i + 1 < len(nums) and (dfs(i+1, target - nums[i]) or 
            (dfs(i+1, target))):
                return True
            cache[(i, target)] = False
            return cache[(i, target)]
        
        return dfs(0, target)