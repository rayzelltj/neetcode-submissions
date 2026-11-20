class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            maxDiff = max(maxDiff, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return maxDiff