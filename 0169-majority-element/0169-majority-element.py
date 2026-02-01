class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        print(hashmap)
        res = 0
        ans = 0
        for k, v in hashmap.items():
            if hashmap[k] > res:
                res = v
                ans = k

        return ans

        