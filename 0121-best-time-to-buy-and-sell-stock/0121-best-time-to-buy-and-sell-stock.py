class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float("inf")

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit

        

'''
1. profit = sell max - buy min
2. maxProfit, by storing min value, keep track of difference
'''