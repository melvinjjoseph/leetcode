# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        vals=[]
        while(head):
            vals.append(head.val)
            head=head.next
        maxVal=vals[0]+vals[-1]
        for i in range(0,len(vals)//2):
            maxVal=max(maxVal,vals[i]+vals[-1-i])
        return maxVal