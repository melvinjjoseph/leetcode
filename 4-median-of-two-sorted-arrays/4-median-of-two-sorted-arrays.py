class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        if len(nums)%2==1:
            ind=len(nums)-1
            return(nums[ind//2])
        else:
            ind=len(nums)//2
            return((nums[ind]+nums[ind-1])/2)