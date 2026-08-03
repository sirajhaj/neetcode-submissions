class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        l,r=0,n-1
        t=n-1

        while t >= 0 :

            if (-1*nums[l]) < nums[r] :
                res[t] = nums[r]**2
                r-=1
            else :
                res[t] = nums[l]**2
                l+=1
            t-=1
        
        return res