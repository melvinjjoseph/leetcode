class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return x
        i=1
        while(((i+1)*(i+1))<=x):
            i+=1
        return i