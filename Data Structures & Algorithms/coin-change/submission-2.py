class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = amount
        k = len(coins)
        dp = [0]*(n+1)

        for i in range(k):
            if coins[i] > n : continue
            dp[coins[i]] = 1
        
        for i in range(1,n+1):
            if dp[i] == 1 : continue
            valid = -1
            dp[i] = float('inf')
            for j in range(k):
                if i - coins[j] < 0 or dp[i - coins[j]] == -1:
                    continue
                valid = 1
                dp[i] = min(dp[i],dp[i - coins[j]]+1)
            if valid == -1 :
                dp[i] = -1
        
        return dp[n]
                


        