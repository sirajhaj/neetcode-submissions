class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r=0,n-1

        while l < r :
            if nums[l]%2 :
                nums[l],nums[r] = nums[r],nums[l]
                r-=1
            else :
                l+=1
        return nums
        