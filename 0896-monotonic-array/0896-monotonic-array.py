class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev=nums[0]
        inc=0
        for i in range(1,len(nums)):
            if inc==1 and nums[i]<prev:
                return False
            elif inc==-1 and nums[i]>prev:
                return False
            if not inc:
                if prev>nums[i]:
                    inc=-1
                elif prev<nums[i]:
                    inc=1
            prev=nums[i]
        return True