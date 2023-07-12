class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minCost=0
        minHeap=[]
        visit=set()
        def addCosts(n):
            for i in range(len(points)):
                if i not in visit:
                    cost=abs(points[n][0]-points[i][0])+abs(points[n][1]- points[i][1])
                    heapq.heappush(minHeap,[cost,i])
        visit.add(0)
        addCosts(0)
        while len(visit)!=len(points):
            cost,point=heapq.heappop(minHeap)
            if point in visit:
                continue
            minCost+=cost
            visit.add(point)
            addCosts(point)
        return minCost
            