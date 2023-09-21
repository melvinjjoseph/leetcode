class Solution:
    def reverseWords(self, s: str) -> str:
        l1=s.split()
        op=''
        for i in range(len(l1)-1,-1,-1):
            op+=l1[i]
            if i!=0:
                op+=' '
            
        return op