class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(speed) -> bool:

            currSum = 0

            for pile in piles:
                currSum += math.ceil(pile / speed)

            return currSum <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left