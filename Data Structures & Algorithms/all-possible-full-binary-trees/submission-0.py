class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:

        
        if n%2 == 0 :
            return []
        
        def build(n):
            if n == 1 :
                return [TreeNode(0,None,None)]
            ans = []
            for i in range(1,n-1,2):
                for left in build(i):
                    for right in build(n-i-1):
                        ans.append(TreeNode(0,left,right))
            return ans
        
        return build(n)


        

