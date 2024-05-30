class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j]==0:
                    if i==m-1 and j==n-1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i+1][j]+dp[i][j+1]
        print(dp)
        return dp[0][0]