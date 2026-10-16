class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)
        
        if n == 1 :
            return nums[0]
        elif n==2 :
            return max(nums[0],nums[1])

        def rob2(start,end):
            dp = [0]*n

            dp[start] = nums[start]
            dp[start+1] = max(dp[start],nums[start+1])

            for i in range(start+2,end+1):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            
            return dp[end]


        return max(rob2(0,n-2),rob2(1,n-1))

        