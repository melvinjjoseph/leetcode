class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        maxNum=1
        minNum=1
        for i in nums:
            if i==0:
                maxNum, minNum=1,1
                continue
            tmp=maxNum
            maxNum=max(i*minNum, i*maxNum, i)
            minNum=min(i*minNum, i*tmp, i)
            res=max(maxNum,res)
        return res