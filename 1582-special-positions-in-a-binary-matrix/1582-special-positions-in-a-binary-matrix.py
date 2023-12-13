class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows=[0]*len(mat)
        cols=[0]*len(mat[0])
        for i in range(len(mat)):
            for j in mat[i]:
                if j==1:
                    rows[i]+=1
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i]==1:
                    cols[i]+=1
        res=0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==1 and rows[row]==1 and cols[col]==1:
                    res+=1
        return res