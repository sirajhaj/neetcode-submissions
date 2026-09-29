class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = amount
        k = len(coins)
        memo = {}

        def rec(i):
            if i in memo : return memo[i]
            
            if i <= 0 : return 0
            valid = -1
            res = float('inf')
            
            for j in range(k):
                if i - coins[j] < 0 :
                    continue
                tmp =rec(i - coins[j])
                if tmp == -1:
                    continue 
                valid = 1
                res = min(res,tmp+1)
            
            if valid == -1 : 
                memo[i] = -1
                return -1
            memo[i] = res
            return res
        
        return rec(n)
                


        