class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ind = 0

        while ind < len(nums) - 1 and nums[ind] <= nums[ind + 1]:
            ind += 1
        if target >= nums[0]:
            x = bisect_left(nums, target, 0, ind)
        else:
            x = bisect_left(nums, target, ind + 1, len(nums) - 1)
        if x > len(nums) - 1 or nums[x] != target:
            return False
        return True