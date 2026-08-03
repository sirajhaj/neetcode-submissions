class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_num1 = set(nums1)
        set_num2 = set(nums2)


        res = [[],[]]

        
        for num1 in set_num1 :
            if num1 not in set_num2 :
                res[0].append(num1)
            
        for num2 in set_num2 :
            if num2 not in set_num1 :
                res[1].append(num2)
        return res
        
        