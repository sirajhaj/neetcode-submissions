"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return [] 
        res =[]
        stack = [root]

        cur = root

        while stack :
            cur = stack.pop()
            res.append(cur.val)
            if not cur.children:
                continue
            for child in cur.children:
                stack.append(child)
        res.reverse()
        return res
            



        