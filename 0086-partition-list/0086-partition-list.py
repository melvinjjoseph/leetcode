# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead,greatHead=None,None
        less, great=None, None
        while head:
            if head.val<x:
                if lessHead:
                    less.next=ListNode(head.val,None)
                    less=less.next
                    head=head.next
                else:
                    lessHead=ListNode(head.val,None)
                    less=lessHead
                    head=head.next
            else:
                if greatHead:
                    great.next=ListNode(head.val,None)
                    great=great.next
                    head=head.next
                else:
                    greatHead=ListNode(head.val,None)
                    great=greatHead
                    head=head.next
        if not lessHead:
            return greatHead
        less.next=greatHead
        return lessHead