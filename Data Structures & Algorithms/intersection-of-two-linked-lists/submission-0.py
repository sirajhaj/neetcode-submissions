# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a = headA
        b = headB

        a_length = 0
        while a != None :
            a = a.next
            a_length += 1
        b_length = 0
        while b != None :
            b = b.next
            b_length += 1
        a = headA
        b = headB
        if a_length < b_length :
            for _ in range(b_length - a_length):
                b = b.next
        else :
            for _ in range(a_length - b_length) :
                a = a.next

        while (a != None) and (b != None) :
            if a == b :
                return a
            a = a.next
            b = b.next
        return None
        