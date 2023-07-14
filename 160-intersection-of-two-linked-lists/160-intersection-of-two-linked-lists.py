# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr=headA
        hashSet=set()
        while ptr:
            hashSet.add(ptr)
            ptr=ptr.next
            
        ptr=headB
        while ptr:
            if ptr in hashSet:
                return ptr
            ptr=ptr.next
        return ptr