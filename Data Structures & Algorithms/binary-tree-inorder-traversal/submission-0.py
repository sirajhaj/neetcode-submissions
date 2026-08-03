# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def rec_inorder(root):
            if not root :
                return 
            rec_inorder(root.left)
            res.append(root.val)
            rec_inorder(root.right)
        
        rec_inorder(root)
        return res
    
        