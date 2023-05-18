class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        isIncoming=[False]*(n)
        op=[]
        for i in edges:
            isIncoming[i[1]]=True
        for i in range(len(isIncoming)):
            if isIncoming[i]==False:
                op.append(i)
        return op
        