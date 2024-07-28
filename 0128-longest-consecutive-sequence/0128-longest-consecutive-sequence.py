class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        count = 0

        for i in range(len(nums)):
            mp[nums[i]] = i

        for num in nums:
            if num - 1 not in mp:
                curr = num
                count += 1

                while curr + 1 in mp:
                    curr = curr + 1
                    count += 1
                res = max(res, count)
                count = 0
        return res
            

        