class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols=len(matrix), len(matrix[0])
        zero0=False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        zero0=True
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(rows):
                matrix[i][0]=0
        
        if zero0:
            for j in range(cols):
                matrix[0][j]=0
                