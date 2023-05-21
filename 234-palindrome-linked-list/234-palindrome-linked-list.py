# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data=[]
        while(head):
            data.append(head.val)
            head=head.next
        l=0
        r=len(data)-1
        print(data)
        while(l<=r):
            if data[l]!=data[r]:
                return False
            elif l==r:
                return True
            else:
                l+=1
                r-=1
        return True
                