class Solution:
    def climbStairs(self, n: int) -> int:
        var1=1
        var2=1
        while n:
            n-=1
            tmp=var1+var2
            var1=var2
            var2=tmp
        return var1