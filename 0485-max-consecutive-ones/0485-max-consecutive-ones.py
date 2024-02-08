class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        isprev=False
        max_count=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1 and not isprev:
                isprev=True
                count+=1
                max_count=max(count,max_count)
            elif nums[i]==1:
                count+=1
                max_count=max(count,max_count)
            elif nums[i]==0:
                count=0
                isprev=False
        return max_count
                