class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0: return 0

        left,right = 0,n-1

        while left <= right :
            if nums[right] == val :
                right -= 1
            elif nums[left] == val :
                nums[right],nums[left] = nums[left],nums[right]
                left +=1
                right -=1
            else :
                left +=1
        return left