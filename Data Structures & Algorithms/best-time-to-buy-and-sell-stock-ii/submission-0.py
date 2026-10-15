class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        min_i = 0
        max_profit = 0

        for i in range(1,n):
            diff = prices[i]-prices[min_i]
            if diff > 0 :
                max_profit +=diff    
            min_i = i
        
        return max_profit
        