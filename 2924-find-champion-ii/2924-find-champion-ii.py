class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees=defaultdict(int)
        for a,b in edges:
            indegrees[b]+=1
        res=-1
        for i in range(n):
            if indegrees[i]==0 and res!=-1:
                return -1
            elif indegrees[i]==0:
                res=i
        return res 