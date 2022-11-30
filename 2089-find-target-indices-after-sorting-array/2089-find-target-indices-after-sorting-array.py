class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ind=[]
        nums.sort()
        i=0
        while(target in nums):
            ind.append(nums.index(target)+i)
            nums.remove(target)
            i=i+1
        return ind