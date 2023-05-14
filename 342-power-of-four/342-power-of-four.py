class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        i=0
        while(4**i<n):
            i+=1
        if 4**i==n:
            return True
        return False