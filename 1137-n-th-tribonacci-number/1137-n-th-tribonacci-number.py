class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0,1,1]
        for i in range(n-1):
            new=dp[-1]+dp[-2]+dp[-3]
            dp.append(new)
        return dp[n]