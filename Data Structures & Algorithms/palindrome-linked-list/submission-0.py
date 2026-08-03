# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head 
        stack = []
        while p :
            stack.append(p.val)
            p = p.next
        
        p = head
        while stack :
            if stack.pop() != p.val :
                return False
            p = p.next
        
        return True 

        