class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = defaultdict(int)
        ans = []

        for i in range(len(nums)):
            mp[nums[i]] += 1
        
        sorted_map = sorted(mp.items(), key=lambda item: item[1], reverse=True)
        for key, v in sorted_map:
            if k != 0:
                ans.append(key)
                k -= 1
        return ans

        