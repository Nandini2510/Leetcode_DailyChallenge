class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0

        while res < len(nums) - 1 and nums[res] < nums[res + 1]:
            res += 1
        if target >= nums[0]:
            x = bisect_left(nums, target, 0, res)
        else:
            x = bisect_left(nums, target, res + 1, len(nums) - 1)
        if x > len(nums) - 1:
            return -1
        return x if nums[x] == target else -1
        