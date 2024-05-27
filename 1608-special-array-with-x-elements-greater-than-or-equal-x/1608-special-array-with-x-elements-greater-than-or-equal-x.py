class Solution:
    def binarySearch(self, nums, val):
        l = 0
        h = len(nums) - 1

        index = len(nums)

        while l <= h:
            mid = (l+h) // 2

            if nums[mid] >= val:
                index = mid
                h = mid - 1
            else:
                l = mid + 1
        return index
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        N = len(nums)
        for i in range(1, N + 1):
            k = self.binarySearch(nums, i)
            if N - k == i:
                return i
        return -1
         
