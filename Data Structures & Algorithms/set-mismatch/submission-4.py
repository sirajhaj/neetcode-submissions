class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n= len(nums)
        repeated = 0
        for i in range(n):
            if nums[abs(nums[i])-1] < 0 :
                repeated = abs(nums[i])
            nums[abs(nums[i])-1]*=-1
        
        res = [repeated]
        nums[repeated-1] = 0
        for i in range(n):
            if nums[i] > 0 :
                res.append(i+1)
        
        return res
        
        