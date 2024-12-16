class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap=[(nums[i],i) for i in range(len(nums))]
        heapq.heapify(min_heap)
        
        for _ in range(k):
            val,i=heapq.heappop(min_heap)
            heappush(min_heap,(val*multiplier,i))
            nums[i]=val*multiplier
        # while min_heap:
        #     val,i=heapq.heappop(min_heap)
        #     nums[i]=val
        return nums