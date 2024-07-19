class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        res = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                curr_name = num
                count += 1
                while curr_name + 1 in num_set:
                    curr_name += 1
                    count += 1
                res = max(res, count)
                count = 0
        return res

