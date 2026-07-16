class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for i in range(1,len(prices)-1):
        # i=1
        # while i < len(prices-1)
        #     if prices
        maxP = 0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > maxP:
                    maxP = prices[j] - prices[i]
        return maxP