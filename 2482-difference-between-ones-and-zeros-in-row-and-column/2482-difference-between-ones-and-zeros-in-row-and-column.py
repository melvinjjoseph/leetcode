class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows=[0]*len(grid)
        cols=[0]*len(grid[0])
        for row in range(len(rows)):
            for col in range(len(cols)):
                rows[row]+=grid[row][col]
                cols[col]+=grid[row][col]
        diff=[[0]*len(cols) for i in rows]
        print(rows,cols)
        for row in range(len(rows)):
            for col in range(len(cols)):
                diff[row][col]= 2*rows[row]+2*cols[col]-len(rows)-len(cols)
    
        return diff
        