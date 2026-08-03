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
            
            res1 = dfs(root.left,True)+dfs(root.right,True)
            res2 = dfs(root.left,False)+dfs(root.right,False)
            res3 = dfs(root.left,True)+dfs(root.right,False)
            res4 = dfs(root.left,False)+dfs(root.right,True)
            res = max(res1,res2,res3,res4)

            memo[(root,False)] = res

            return res
        
        return max(dfs(root,True),dfs(root,False))
        