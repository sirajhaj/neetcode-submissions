class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)

        sum_nums = 0
        sum_global = 0
        for i in range(1,n+1):
            sum_global+=i
        for i in range(n):
            sum_nums+=nums[i]
        
        
        return sum_global-sum_nums 
        