class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        
        def build(lo,hi):
            if lo > hi :
                return [None]
            ans = []

            for val in range(lo,hi+1):
                for left in build(lo,val-1):
                    for right in build(val+1,hi):
                        ans.append(TreeNode(val,left,right))
            return ans


        return build(1,n)

