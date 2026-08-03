class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        l,r=0,n-1
        t=n-1

        while t >= 0 :
            p1 = nums[l]**2
            p2 = nums[r]**2

            if p1 < p2 :
                res[t] = p2
                r-=1
            else :
                res[t] = p1
                l+=1
            t-=1
        
        return res