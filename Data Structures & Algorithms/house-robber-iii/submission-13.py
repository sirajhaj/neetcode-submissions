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
        
        def max_sum(node):
            
            left_not = left_taken = right_not = right_taken = 0

            if node.left :
                left_not = memo[node.left][0]
                left_taken = memo[node.left][1]
            if node.right:
                right_not = memo[node.right][0]
                right_taken = memo[node.right][1]

            return (max(left_not,left_taken) + max(right_not,right_taken),
                    left_not + right_not + node.val)


        def dfs_post(root):
            if not root:
                return
            
            dfs_post(root.left)
            dfs_post(root.right)

            memo[root] = max_sum(root)


        
        dfs_post(root)
        return max(memo[root][0],memo[root][1])
        