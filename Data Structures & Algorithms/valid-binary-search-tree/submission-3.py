# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        isValid = [True]
        def dfs(root):
            
            res_left = [root.val,root.val]
            res_right = [root.val,root.val]

            if root.left:

                res_left = dfs(root.left)
                if root.val <= res_left[1] :
                    isValid[0] = False  
                    
            if root.right:

                res_right = dfs(root.right)
                if root.val >= res_right[0] :
                    isValid[0] = False 
            
            return [res_left[0],res_right[1]]
        
        dfs(root)
        return isValid[0]

        