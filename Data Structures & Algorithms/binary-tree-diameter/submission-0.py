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
            if not root.left and not root.right :
                return 0
            len_left = maxlength(root.left)
            len_right = maxlength(root.right)

            cur_diameter = 0
            if root.left and root.right :
                cur_diameter = len_left+len_right+2
            elif root.left :
                cur_diameter = len_left+1
            elif root.right:
                cur_diameter = len_right+1

            diameter[0] = max(diameter[0],cur_diameter)
            return max(len_left,len_right)+1
        
        maxlength(root)
        return diameter[0]
        