class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l,r =1,1

        while r < n :
            while r < n and nums[r] == nums[l-1]:
                r+=1
            if r>=n :
                break
            nums[l]=nums[r]
            l+=1
            r+=1
        return l
        