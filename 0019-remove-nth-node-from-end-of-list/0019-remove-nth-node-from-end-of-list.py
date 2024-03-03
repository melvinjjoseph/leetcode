# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        ptr=head
        count=0
        while(ptr):
            ptr=ptr.next
            count+=1
        if count==n:
            return head.next
        n=count-n-1
        count=0
        ptr=head
        while(ptr!=None):
            if count==n:
                ptr.next=ptr.next.next
            count+=1
            ptr=ptr.next
        
        return head
        
        