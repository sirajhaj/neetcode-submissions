# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return True
            
            left_del = dfs(root.left) 
            right_del = dfs(root.right)

            if left_del :
                root.left = None
            if right_del :
                root.right = None
            
            if not root.right and not root.left :
                if root.val == target:
                    return True
            
            return False
        
        
        if dfs(root) == True :
            return None
        
        return root
        