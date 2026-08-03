"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res =[]

        def rec(root):
            if not root :
                return 
            
            if root.children :
                for child in root.children:
                    rec(child)
            res.append(root.val)
        
        rec(root)
        return res
        