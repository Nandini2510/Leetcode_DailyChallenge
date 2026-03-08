class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countMap = Counter(nums)
        zeros, ones, twos = countMap[0], countMap[1], countMap[2]
        
        i = 0
        while zeros:
            nums[i] = 0
            i += 1
            zeros -=1
        
        while ones:
            nums[i] = 1
            i += 1
            ones -= 1
        
        while twos:
            nums[i] =2
            i += 1
            twos -= 1
