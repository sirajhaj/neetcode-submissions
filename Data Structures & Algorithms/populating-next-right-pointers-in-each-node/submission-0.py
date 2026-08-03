"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return root
        
        def traversal(node1,node2):
            
            while node1.right and node2.left :
                node1.right.next = node2.left
                node1 = node1.right
                node2 = node2.left
            
        def dfs(node):
            if not node or not node.left or not node.right:
                return  
            
            node.left.next = node.right
            traversal(node.left,node.right)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return root

        