class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-1*nums[i]
        heapq.heapify(nums)
        while k>0:
            res=heapq.heappop(nums)
            k-=1
        return res*-1