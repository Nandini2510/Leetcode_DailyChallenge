class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashmap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                res.append(i)
                res.append(hashmap[target - nums[i]])
            else:
                hashmap[nums[i]] = i
        return res