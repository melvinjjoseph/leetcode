class Solution:
    def findMax(self,grid, x ,y):
        maxEle=0
        for i in range(x,x+3):
            for j in range(y,y+3):
                maxEle=max(maxEle, grid[i][j])
        return maxEle
    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N=len(grid)
        maxGrid=[[0] * (N-2) for i in range(N-2)]
        for i in range(N-2):
            for j in range(N-2):
                maxGrid[i][j]=self.findMax(grid,i,j)
        return maxGrid