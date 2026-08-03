# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]
        def maxlength(root):
            if not root:
                return 0
            
            len_left = maxlength(root.left)
            len_right = maxlength(root.right)

            diameter[0] = max(diameter[0],len_left+len_right)
            return max(len_left,len_right)+1
        
        maxlength(root)
        return diameter[0]
        