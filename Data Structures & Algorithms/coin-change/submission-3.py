class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = amount
        k = len(coins)
        dp = [amount+1]*(n+1)
        dp[0] = 0
        
        
        for i in range(1,n+1):
            
            for j in range(k):
                if i - coins[j] < 0 :
                    continue
                dp[i] = min(dp[i],dp[i - coins[j]]+1)
        
        
        return dp[n] if dp[n] != n+1 else -1
                


        