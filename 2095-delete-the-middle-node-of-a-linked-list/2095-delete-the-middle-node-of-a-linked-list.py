# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        slow=head
        fast=head
        if head.next is None:
            return None
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
        return head