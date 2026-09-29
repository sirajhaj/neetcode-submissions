class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax , curMin = 1 , 1

        for num in nums : 
            if num == 0 :
                curMax , curMin = 1 , 1
            tmp = curMax
            curMax = max(num*curMax,num*curMin,num)
            curMin = min(num*tmp,num*curMin,num)

            res = max(res,curMax)

        return res
        