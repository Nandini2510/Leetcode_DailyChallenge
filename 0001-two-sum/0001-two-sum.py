class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        mp = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in mp:
                ans.append(mp[target - nums[i]])
                ans.append(i)
            else:
                mp[nums[i]] = i
        return ans
        