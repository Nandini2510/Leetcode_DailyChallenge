class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        for key, val in mp.items():
            heapq.heappush(heap, (-1*val, key))
        
        while k > 0:
            val, key = heapq.heappop(heap)
            ans.append(key)
            k -= 1
        return ans


