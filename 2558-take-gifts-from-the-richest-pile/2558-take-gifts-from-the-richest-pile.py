class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap=[]
        for gift in gifts:
            heapq.heappush(max_heap,-gift)
        for _ in range(k):
            maxi=-heapq.heappop(max_heap)
            maxi=maxi**0.5
            maxi=int(maxi)
            heapq.heappush(max_heap,-maxi)
        return abs(sum(max_heap))