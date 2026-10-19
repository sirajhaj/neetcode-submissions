class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        l,r = 0,0
        count = 0

        while l < n-1 and r < n-1 and l <= r:
            farthest = r
            for i in range(l,r+1):
                if nums[i] + i > farthest :
                    farthest = nums[i] + i
            l = r+1
            r = farthest
            count += 1

        if r < n-1 and l > r :
            return -1  
        return count