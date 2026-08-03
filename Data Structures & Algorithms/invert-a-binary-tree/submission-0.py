# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs_invert(root):
            if not root :
                return root
            
            right_child = dfs_invert(root.left)
            left_child = dfs_invert(root.right)
            root.left = left_child
            root.right = right_child
            return root
        
        return dfs_invert(root)
        