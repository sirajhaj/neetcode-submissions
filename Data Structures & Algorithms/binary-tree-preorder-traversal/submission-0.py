# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rec_preorder(root):
            if not root :
                return 
            res.append(root.val)
            rec_preorder(root.left)
            rec_preorder(root.right)
        
        rec_preorder(root)
        return res
        