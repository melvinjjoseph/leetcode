# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        cur=head
        while cur!=None:
            stack.append(cur)
            cur=cur.next
        cur=stack.pop()
        maxi=cur.val
        result=ListNode(maxi)
        while stack:
            cur=stack.pop()
            if cur.val<maxi:
                continue
            new=ListNode(cur.val)
            new.next=result
            result=new
            maxi=cur.val
        return result