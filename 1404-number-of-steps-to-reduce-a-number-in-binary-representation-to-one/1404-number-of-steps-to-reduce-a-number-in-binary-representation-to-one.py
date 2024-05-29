class Solution:
    def numSteps(self, s: str) -> int:
        carry=0
        op=0
        for i in range(len(s)-1,0,-1):
            digit=int(s[i])+carry
            if digit%2==0:
                op+=1
            else:                
                carry=1
                op+=2
        return op+carry