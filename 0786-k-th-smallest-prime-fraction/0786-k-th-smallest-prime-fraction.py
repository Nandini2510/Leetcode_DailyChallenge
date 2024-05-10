class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        mp = {}
        res = ()
        n = len(arr)
      

        for i in range(n):
            for j in range(i+1, n):
                val = arr[i] / arr[j]
                mp[val] = (arr[i], arr[j])

       
        for key, value in mp.items():
            heapq.heappush(heap, (key, value))
        while k > 0:
            pop_key, pop_pair = heapq.heappop(heap)
        
            res = pop_pair
            k -= 1
        return list(res)



