class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            if nums[mid]>=nums[l]:   #in the left sorted protion
                if target>nums[mid]:
                    l=mid+1
                elif target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:                      #in the right sorted portion
                if target>nums[r]:
                    r=mid-1
                elif target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
                
        