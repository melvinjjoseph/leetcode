class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        res=[]
        k=0
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(original[k])
                k+=1
            res.append(t)
        return res