class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n=len(edges1)+1
        m=len(edges2)+1
        
        def buildadj(edges):
            adj=defaultdict(list)
            for u,v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adj1=buildadj(edges1)
        adj2=buildadj(edges2)
        
        def getDiameter(cur,par,adj):
            max_paths=[0,0]
            max_dia=0
            
            for nei in adj[cur]:
                if nei==par:
                    continue
                nei_d, nei_max=getDiameter(nei,cur,adj)
                max_dia=max(max_dia,nei_d)
                
                heapq.heappush(max_paths, nei_max)
                heapq.heappop(max_paths)
            
            max_dia=max(max_dia, sum(max_paths))
            return max_dia,1+max(max_paths)
        d1,_=getDiameter(0,-1,adj1)
        d2,_=getDiameter(0,-1,adj2)
        
        return max(d1,d2,1+ math.ceil(d1/2)+ math.ceil(d2/2))