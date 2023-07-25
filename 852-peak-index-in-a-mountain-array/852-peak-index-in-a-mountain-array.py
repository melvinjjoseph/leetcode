class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0 
        r=len(arr)
        while(l<r):
            mid=(l+r)//2
            if arr[mid]>=arr[mid+1]:
                r=mid
            else:
                l=mid+1
        return l