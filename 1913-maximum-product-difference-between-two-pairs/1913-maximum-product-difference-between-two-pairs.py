class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1=max(nums)
        nums.remove(max1)
        max2=max(nums)
        nums.remove(max2)
        min1=min(nums)
        nums.remove(min1)
        min2=min(nums)
        nums.remove(min2)
        return max1*max2-min1*min2
        