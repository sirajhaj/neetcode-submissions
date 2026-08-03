# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rec_postorder(root):
            if not root :
                return 
            
            rec_postorder(root.left)
            rec_postorder(root.right)
            res.append(root.val)
        
        rec_postorder(root)
        return res
        