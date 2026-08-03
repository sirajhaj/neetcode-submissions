# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        
        memo = {}
        def dfs(root,taken):
            if not root:
                return 0
            if (root,taken) in memo :
                return memo[(root,taken)]
            
            if taken :
                memo[(root,True)] = dfs(root.left,False)+dfs(root.right,False)+root.val
                return memo[(root,True)]
            
            left_taken = dfs(root.left,True)
            left_not = dfs(root.left,False)
            right_taken = dfs(root.right,True)
            right_not = dfs(root.right,False)
            
            res1 = left_taken + right_taken
            res2 = left_not + right_not
            res3 = left_taken + right_not
            res4 = left_not + right_taken
            
            res = max(res1,res2,res3,res4)

            memo[(root,False)] = res

            return res
        
        return max(dfs(root,True),dfs(root,False))
        