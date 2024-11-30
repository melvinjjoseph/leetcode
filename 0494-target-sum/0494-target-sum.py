class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        
        def back(i,tot):
            if i==len(nums) and tot==target:
                return 1
            elif i==len(nums):
                return 0
            if (i,tot) in dp:
                return dp[(i,tot)]
            dp[(i,tot)]=back(i+1,tot+nums[i])+back(i+1,tot-nums[i])
            return dp[(i,tot)]
        return back(0,0)