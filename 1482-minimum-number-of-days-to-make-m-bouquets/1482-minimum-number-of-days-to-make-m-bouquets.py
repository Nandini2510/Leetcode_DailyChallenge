class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(days):
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        left, right = 1, max(bloomDay)
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res