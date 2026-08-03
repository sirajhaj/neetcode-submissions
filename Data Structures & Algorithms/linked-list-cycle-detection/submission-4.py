# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None :
            return False
        if head.next.next == head :
            return True
        
        p1 = head
        p2 = head.next.next

        while p2 and p2.next :
            if p2.next == p1 or p2 == p1.next:
                return True
            p1 = p1.next
            p2 = p2.next.next
            
        
        return False


        