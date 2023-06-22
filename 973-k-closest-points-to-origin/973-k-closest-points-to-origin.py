class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for ele in points:
            dis=ele[0]**2+ele[1]**2
            minHeap.append([dis,ele[0],ele[1]])
        heapq.heapify(minHeap)
        while k>0:
            popped=heapq.heappop(minHeap)
            res.append([popped[1],popped[2]])
            k-=1
        return res
                        