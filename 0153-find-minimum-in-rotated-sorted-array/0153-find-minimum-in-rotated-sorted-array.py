class Solution:
    def findMin(self, nums: List[int]) -> int:

        def feasible(mid) -> bool:
            return nums[mid] < nums[right]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return nums[left]
        