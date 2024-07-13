class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                count = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1
                
                res = max(res, count)
        return res
            

        