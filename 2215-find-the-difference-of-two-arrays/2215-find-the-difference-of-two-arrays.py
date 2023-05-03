class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        set1=set(nums1)
        set2=set(nums2)
        l1=set1-set2
        l2=set2-set1
        return [l1,l2]
        