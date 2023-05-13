class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<0:
            return False
        i=0
        while(3**i<n):
            i+=1
        if 3**i==n:
            return True
        return False