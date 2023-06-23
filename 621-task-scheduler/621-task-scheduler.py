class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskSet=Counter(tasks)
        maxHeap=[-cnt for cnt in taskSet.values()]
        heapq.heapify(maxHeap)
        time=0
        q=collections.deque()
        while(maxHeap or q):
            time+=1
            if maxHeap:
                popped=heapq.heappop(maxHeap)
                popped+=1
                if popped<0:
                    q.append([popped,time+n])
            
            if q and q[0][1]==time:
                popped=q.popleft()
                heapq.heappush(maxHeap,popped[0])
        return time