# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root :
            return False
        
        def dfs(root,target):
            if not root.left and not root.right:
                if (target-root.val) ==0:
                    return True
                else:
                    return False 
            elif not root.left :
                return dfs(root.right,target-root.val)
            elif not root.right:
                return dfs(root.left,target-root.val)
            
            return dfs(root.left,target-root.val) or dfs(root.right,target-root.val) 
        return dfs(root,targetSum)
            

        