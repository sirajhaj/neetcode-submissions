# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        ancestor = [root]
        lowest = [False]

        def dfs(node):
            if not node :
                return False
            
            anc = (node.val == p.val or node.val == q.val)
            
            left = dfs(node.left)
            right = dfs(node.right)

            if not lowest[0] :
                if anc and (left or right) :
                    ancestor[0] = node
                    lowest[0] = True
                elif left and right :
                    ancestor[0] = node
                    lowest[0] = True
            return anc or left or right
        
        dfs(root)
        return ancestor[0]


                
            
        