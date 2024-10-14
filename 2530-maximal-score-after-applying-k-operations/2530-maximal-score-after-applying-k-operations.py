class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap=[]
        score=0
        for num in nums:
            heapq.heappush(maxHeap,-num)
        for _ in range(k):
            popped=heapq.heappop(maxHeap)
            popped=abs(popped)
            score+=popped
            popped=math.ceil(popped/3)
            heapq.heappush(maxHeap, -popped)
        return score