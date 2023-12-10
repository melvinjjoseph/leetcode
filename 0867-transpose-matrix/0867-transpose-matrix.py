class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            tmp=[]
            for j in range(len(matrix)):
                val=matrix[j][i]
                tmp.append(val)
            ans.append(tmp)
        return ans
            