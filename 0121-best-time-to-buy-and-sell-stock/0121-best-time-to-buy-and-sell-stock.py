class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = float("inf")

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProf = max(maxProf, (prices[i] - minPrice))
        return maxProf
        