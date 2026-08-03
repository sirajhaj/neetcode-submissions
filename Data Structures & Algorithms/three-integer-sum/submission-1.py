class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        curr = float("inf")
        res = []

        for i in range(n):
            if nums[i] > 0 :
                break
            if curr == nums[i] :
                continue
            curr = nums[i]
            l,r = i+1,n-1
            target = 0 - curr
            while l < r :
                curSum = nums[l] + nums[r]
                if curSum < target :
                    l+=1
                elif curSum > target :
                    r-=1
                else :
                    res.append([nums[i],nums[l],nums[r]])
                    temp = nums[l]
                    while l<r and nums[l] == temp :
                        l+=1
        return res
                    

                
                
                
