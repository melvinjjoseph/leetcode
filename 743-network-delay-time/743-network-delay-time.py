class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append([v,w])
            
        maxTime=0
        minHeap=[[0,k]]
        visit=set()
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            maxTime=max(maxTime,w1)
            for v1,w in edges[n1]:
                if v1 not in visit:
                    heapq.heappush(minHeap,[w1+w,v1])
        
        return maxTime if len(visit)==n else -1
        