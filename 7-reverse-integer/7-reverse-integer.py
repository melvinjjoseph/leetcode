class Solution:
    def reverse(self, x: int) -> int:
        op=0
        if x>=0:
            while(x>0):
                op=op*10
                op=op+x%10
                x=x//10
        else:
            x=x*-1
            while(x>0):
                op=op*10
                op=op+x%10
                x=x//10
            op=op*-1
        if op>2**31-1 or op<-1*(2**31):
            return 0
        return(op) 

