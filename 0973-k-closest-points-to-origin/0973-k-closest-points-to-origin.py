class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heapify, heappop

        min_heap = []

        for xi, yi in points:
            dist = xi ** 2 + yi ** 2
            min_heap.append((dist, xi, yi))
        heapq.heapify(min_heap)

        res = []

        for i in range(k):
            a, b, c = heapq.heappop(min_heap)
            res.append((b,c))
        return res