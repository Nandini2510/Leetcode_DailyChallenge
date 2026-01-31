class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
            if hashmap[nums[i]] > 1:
                return True
        return False