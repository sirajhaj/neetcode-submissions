# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        bst = []
        def inorder(root) :
            if not root :
                return
            
            inorder(root.left)
            bst.append(root)
            inorder(root.right)
        

        inorder(root)
        n = len(bst)
        first, last= None,None
        if bst[0].val > bst[1].val:
            first = bst[0]
        if bst[n-1].val < bst[n-2].val :
            last = bst[n-1]

        for i in range(1,n-1):
            if not first :
                if bst[i].val > bst[i+1].val or bst[i-1].val > bst[i].val :
                    first = bst[i]
            if not last :
                if bst[n-1-i].val > bst[n-i].val or bst[n-2-i].val > bst[n-1-i].val :
                    last = bst[n-1-i]
        first.val,last.val = last.val,first.val
        return root 



        
        