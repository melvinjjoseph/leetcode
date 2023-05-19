# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1=[]
        li2=[]
        while(l1):
            li1.append(l1.val)
            l1=l1.next
        while(l2):
            li2.append(l2.val)
            l2=l2.next
        num1=0
        for i in range(len(li1)):
            num1=num1*10+li1[-1-i]
        num2=0
        for i in range(len(li2)):
            num2=num2*10+li2[-1-i]
        op=num1+num2
        ophead=ListNode(op%10)
        cur=ophead
        while(True):
            op=op//10
            if op==0:
                return ophead
            else:
                cur.next=ListNode(op%10)
                cur=cur.next
            
            
        