class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in range(len(nums)):
            if counter[nums[i]] > len(nums) / 2:
                return nums[i]

        