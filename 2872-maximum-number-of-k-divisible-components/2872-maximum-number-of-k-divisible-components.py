class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        res=0
        def dfs(cur,parent):
            total=values[cur]
            for child in graph[cur]:
                if child!=parent:
                    total+=dfs(child,cur)
            if total%k==0:
                nonlocal res
                res+=1
            return total
        dfs(0,-1)
        return res