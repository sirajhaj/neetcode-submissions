class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_profit = 0
        index_buy = 0

        for i in range(1,n):
            diff = prices[i] - prices[index_buy]
            if diff < 0 :
                index_buy = i
            elif diff > max_profit :
                max_profit = diff
        
        return max_profit



        