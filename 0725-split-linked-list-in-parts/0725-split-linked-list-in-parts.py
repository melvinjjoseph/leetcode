# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        num=0
        cur=head
        while cur:
            num+=1
            cur=cur.next
        length,add=num//k,num%k
        cur=head
        res=[]
        for i in range(k):
            res.append(cur)
            for i in range(length-1+ (1 if add>0 else 0)):
                if not cur:
                    break
                cur=cur.next
            add-=1
            if cur:
                cur.next,cur=None,cur.next
        return res
                