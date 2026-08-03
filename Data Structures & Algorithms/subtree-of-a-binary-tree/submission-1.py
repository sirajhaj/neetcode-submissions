# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        
        def sameTree(tree1,tree2):
            if not tree1 and not tree2 :
                return True
            elif not tree1 or not tree2 :
                return False
            if tree1.val != tree2.val :
                return False
            return sameTree(tree1.left,tree2.left) and sameTree(tree1.right,tree2.right)



        stack1 = [root]
        visited = set()

        while stack1 :
            curr = stack1.pop()

            if curr.val == subRoot.val :
                if sameTree(curr,subRoot)==True :
                    return True

            if curr not in visited :
                visited.add(curr)
                if curr.right != None :
                    stack1.append(curr.right)
                if curr.left != None :
                    stack1.append(curr.left)
        return False


            
            

        