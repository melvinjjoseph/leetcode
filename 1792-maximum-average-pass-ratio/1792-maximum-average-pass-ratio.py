class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap=[(classes[i][0]/classes[i][1]-(classes[i][0]+1)/(classes[i][1]+1),classes[i][0], classes[i][1]) for i in range(len(classes))]
        heapq.heapify(max_heap)
        for _ in range(extraStudents):
            _,num,den=heapq.heappop(max_heap)
            num+=1
            den+=1
            new_diff=num/den-(num+1)/(den+1)
            heapq.heappush(max_heap, (new_diff,num, den))
        rate=0
        for _,passed,total in max_heap:
            rate+=passed/total
        rate/=len(max_heap)
        return rate
        