class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    l=[i,j]
                    return l
                