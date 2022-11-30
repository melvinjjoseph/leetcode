class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        f=nums.index(target)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                r=i
                break
        return [f,r]    
            