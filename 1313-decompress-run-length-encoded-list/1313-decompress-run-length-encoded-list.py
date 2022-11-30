class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        op=[]
        for i in range(0,len(nums),2):
            val=nums[i+1]
            freq=nums[i]
            for j in range(freq):
                op.append(val)
        return op