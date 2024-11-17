class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=len(nums)+1
        left=0
        window_sum=0
        for right in range(len(nums)):
            window_sum+=nums[right]
            while window_sum>=target:
                res=min(res,right-left+1)
                window_sum-=nums[left]
                left+=1
        return res if res!=len(nums)+1 else 0