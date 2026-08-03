# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        def dfs_post(root):
            if not root:
                return (0,0)
            
            left = dfs_post(root.left)
            right = dfs_post(root.right)
            
            return (left[1]+right[1]+root.val , max(left[0],left[1]) + max(right[0],right[1]) )

        
        return max(dfs_post(root)[0],dfs_post(root)[1])
        