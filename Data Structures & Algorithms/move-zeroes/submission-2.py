class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j=0

        while j < n and nums[j] != 0 :
            j+=1
        i = j

        while i < n and j < n :
            if nums[i] == 0 and nums[j] == 0 :
                j+=1
            elif nums[i] == 0 and nums[j] != 0 :
                nums[i] = nums[j]
                nums[j] = 0
                j+=1
                i+=1
            else :
                i+=1
            

        

        