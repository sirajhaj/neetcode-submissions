class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = amount
        k = len(coins)
        dp = [[0] * (n + 1) for _ in range(k)]
        
        for i in range(k):
            dp[i][0] = 1
        
        for j in range(1,n+1):
            if j % coins[0] != 0 :
                dp[0][j] = 0
            else :
                dp[0][j] = 1

        for j in range(1,n+1):
            for i in range(1,k):
                
                dp[i][j] = dp[i-1][j]
                if j - coins[i] >= 0 :
                    dp[i][j] += dp[i][j-coins[i]]
        
        
        return dp[k-1][n]