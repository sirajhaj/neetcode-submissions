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
            
            max_left,min_left = root.val,root.val
            max_right,min_right = root.val,root.val
            if root.left:
                res_left = dfs(root.left)
                max_left,min_left = res_left[1],res_left[0]
                if root.val <= max_left :
                    isValid[0] = False  
            if root.right:
                res_right = dfs(root.right)
                max_right,min_right = res_right[1],res_right[0]
                if root.val >= min_right :
                    isValid[0] = False 
            
            return [min_left,max_right]
        
        dfs(root)
        return isValid[0]

        