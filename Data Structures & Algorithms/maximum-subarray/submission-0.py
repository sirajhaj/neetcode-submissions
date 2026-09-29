class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = float('-inf')
        n = len(nums) 

        curSum = 0
        curMax = float('-inf')
        
        for i in range(0,n):
            if curSum < 0 :
                curSum = 0
            curSum += nums[i]
            curMax = max(curSum,curMax)
            res = max(res,curMax)    

        return res
        