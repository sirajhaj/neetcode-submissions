class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        memo = {}
        
        def path(start):
            if start in memo :
                return memo[start]
            if start == n-1 :
                return True
            if start < n-1 and nums[start]==0 :
                return False 

            for i in range(1,nums[start]+1):
                if path(start+i) :
                    memo[start] = True
                    return True
            memo[start] = False
            return False  
        

        return path(0)
        