class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = defaultdict(int)
        ans = []

        for i in range(len(nums)):
            mp[nums[i]] += 1
        
        sorted_map = sorted(mp.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_map[:k]]

        