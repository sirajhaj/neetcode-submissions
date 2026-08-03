# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root :
            return 0
        
        def dfs(root,mx) :
            if not root :
                return 0
            res = 0
            cur_mx = mx
            if root.val >= mx :
                cur_mx = root.val
                res = 1
            return res + dfs(root.left,cur_mx) + dfs(root.right,cur_mx)
        
        return dfs(root,root.val)
        