class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtab={}
        for i in range(len(nums)):
            if nums[i] not in hashtab:
                hashtab[nums[i]]=i
            else:
                ind=hashtab[nums[i]]
                if (i-ind)<=k:
                    return True
                hashtab[nums[i]]=i
        return False