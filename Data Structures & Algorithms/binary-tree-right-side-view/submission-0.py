# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        max_dep = [0]

        def dfs(root,dep):
            if not root :
                return 
            
            if dep > max_dep[0] :
                res.append(root.val)
                max_dep[0] = dep
            dfs(root.right,dep+1)
            dfs(root.left,dep+1)
        
        dfs(root,1)
        return res
            
            

        