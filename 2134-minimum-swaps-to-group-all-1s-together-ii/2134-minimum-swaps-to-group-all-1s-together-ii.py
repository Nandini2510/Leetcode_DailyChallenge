class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        # find the window with max number of 1's, so we can take len(window) - max(1s)
        # For circular part, we can concatenate the same nums array to itself or to save space we can do nums[r % n] which will give us index at original nums
        """
        n = len(nums)
        total_ones = nums.count(1)
        l = 0
        window_ones = max_window_ones = 0

        for r in range(2*n):
            if nums[r % n]:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l % n]
                l += 1
            
            max_window_ones = max(max_window_ones, window_ones)

        return total_ones - max_window_ones
        