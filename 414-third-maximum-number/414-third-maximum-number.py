class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setNum=set(nums)
        if len(setNum)<=2:
            return max(setNum)
        setNum.discard(max(setNum))
        setNum.discard(max(setNum))
        return max(setNum)
