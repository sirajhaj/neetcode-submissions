# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        if not root :
            return 0
        
        memo = {}
        
        def max_sum(node,taken):
            
            left_not = left_taken = right_not = right_taken = 0

            if node.left :
                left_not = memo[(node.left,False)]
                left_taken = memo[(node.left,True)]
            if node.right:
                right_not = memo[(node.right,False)]
                right_taken = memo[(node.right,True)]

            if taken :
                return left_not + right_not + node.val
            
            res1 = left_taken + right_taken
            res2 = left_not + right_not
            res3 = left_taken + right_not
            res4 = left_not + right_taken

            return max(res1,res2,res3,res4)


        def dfs_post(root):
            if not root:
                return
            
            dfs_post(root.left)
            dfs_post(root.right)

            memo[(root,True)] = max_sum(root,True)
            memo[(root,False)] = max_sum(root,False)

        
        dfs_post(root)
        return max(memo[(root,True)],memo[(root,False)])
        