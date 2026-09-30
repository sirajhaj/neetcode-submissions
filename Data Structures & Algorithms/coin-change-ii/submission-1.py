class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        k = len(coins)
        memo = {}
        def rec(i,amount):
            if (i,amount) in memo :
                return memo[(i,amount)]
            if i == k :
                return 0
            if amount == 0 :
                memo[(i,amount)] = 1
                return memo[(i,amount)]
            if amount < 0 :
                return 0
            memo[(i,amount)] = rec(i+1,amount) + rec(i,amount-coins[i])
            return memo[(i,amount)]
        
        return rec(0,amount)
        