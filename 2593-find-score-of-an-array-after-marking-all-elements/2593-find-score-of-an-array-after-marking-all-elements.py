class Solution:
    def findScore(self, nums: List[int]) -> int:
        min_heap=[(nums[i],i) for i in range(len(nums))]
        heapq.heapify(min_heap)
        marked=[0]*len(nums)
        score=0
        while min_heap:
            val,idx=heapq.heappop(min_heap)
            if marked[idx]:
                continue
            score+=val
            marked[idx]=1
            if idx!=0:
                marked[idx-1]=1
            if idx!=len(nums)-1:
                marked[idx+1]=1
        return score