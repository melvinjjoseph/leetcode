class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        op=[]
        l,t=0,0
        r,b=len(matrix[0]), len(matrix)
        while l<r and t<b:
            for i in range(l,r):
                op.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                op.append(matrix[i][r-1])
            r-=1
            if not (l<r and t<b):
                break
            for i in range(r-1,l,-1):
                op.append(matrix[b-1][i])
            b-=1
            for i in range(b,t-1,-1):
                op.append(matrix[i][l])
            l+=1
        return op