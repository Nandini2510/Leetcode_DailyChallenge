class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mp = {}
        ans = set()

        for i in range(len(nums)):
            target = -1 * nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j = j + 1
        return list(ans)

        