class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)

        for i in range(n):
            nums[i]+=1
        for i in range(n):
            num = abs(nums[i])-1
            if num == n:
                continue
            nums[num]*=-1
        
        for i in range(n):
            if nums[i]>0:
                return i
        return n 
        