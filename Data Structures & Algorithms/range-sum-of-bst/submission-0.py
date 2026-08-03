# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root,l,h):
            if not root:
                return 0
            if root.val >= l and root.val <= h :
                return root.val + dfs(root.left,l,root.val) + dfs(root.right,root.val,h)
            elif root.val < l :
                return dfs(root.right,l,h)
            else:
                return dfs(root.left,l,h)
        return dfs(root,low,high)
        



        