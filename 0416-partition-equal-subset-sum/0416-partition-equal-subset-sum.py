class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(nums, n, subset_sum):
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            if memo[n][subset_sum] != -1:
                return memo[n][subset_sum]
            res = (dfs(nums, n - 1, subset_sum - nums[n-1]) or dfs(nums, n - 1, subset_sum ))
            memo[n][subset_sum] = res
            return res
        
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        n = len(nums)
        memo = [[-1 for _ in range(subset_sum + 1)] for _ in range(n + 1)]
        return dfs(nums, n - 1, subset_sum)