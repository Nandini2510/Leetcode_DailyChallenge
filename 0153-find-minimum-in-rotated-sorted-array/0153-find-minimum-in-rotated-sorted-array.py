class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        res = 5000

        while low <= high:
            mid = (high + low) // 2
            if nums[low] <= nums[mid]:
                res = min(res, nums[low])
                low = mid + 1
            else:
                res = min(res, nums[mid])
                high = mid - 1
        return res
        