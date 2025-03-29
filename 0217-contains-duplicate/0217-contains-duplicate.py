class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in mp:
                return True
            else:
                mp[nums[i]] += 1
        return False
        