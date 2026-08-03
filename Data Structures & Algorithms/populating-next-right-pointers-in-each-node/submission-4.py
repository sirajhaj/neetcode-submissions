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
        if not root or not root.left or not root.right :
            return root

        q = deque([root.left,root.right])
        
        while q:
            n = len(q)-1
            cur = q.popleft()
            later = None
            while n :
                later = q.popleft()
                cur.next = later
                if cur.left :
                    q.append(cur.left)
                if cur.right :
                    q.append(cur.right)
                n-=1
                cur = later
            
            if later.left :
                q.append(later.left)
            if later.right :
                q.append(later.right)

            
            

        return root

        