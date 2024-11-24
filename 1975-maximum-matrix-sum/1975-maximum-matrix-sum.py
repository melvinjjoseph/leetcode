class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negCount=0
        miniVal=float('inf')
        summ=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                summ+=abs(matrix[i][j])
                if matrix[i][j]<0:
                    negCount+=1
                miniVal=min(miniVal, abs(matrix[i][j]))
        if negCount%2==0:
            return summ
        return summ-2*miniVal