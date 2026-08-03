class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n,m = len(nums2),len(nums1)
        greater = {}
        for num in nums1:
            greater[num] = -1
        
        
        stack = []
        for i in range(n-2,-1,-1):
            num = nums2[i+1]
            if nums2[i] < num :
                stack.append(num)
            else :
                while stack :
                    num = stack.pop()
                    if num > nums2[i] :
                        stack.append(num)
                        break
            
            if nums2[i] in greater and num > nums2[i] :
                greater[nums2[i]] = num     

        res = [-1]*m
        for i in range(m):
            res[i] = greater[nums1[i]]
        return res

                

            

        