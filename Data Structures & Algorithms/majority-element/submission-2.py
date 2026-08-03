class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mapp = {}

        for i in range(n):
            if nums[i] in mapp :
                mapp[nums[i]]+=1
            else :
                mapp[nums[i]]=1
            if mapp[nums[i]] > n//2 :
                return nums[i]
        return -1