class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        i=0
        while(2**i<n):
            i+=1
        if 2**i==n:
            return True
        return False