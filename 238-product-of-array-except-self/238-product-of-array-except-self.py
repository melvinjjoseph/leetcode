class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[1]
        num=1
        for i in range(len(nums)-1):
            num=num*nums[i]
            op.append(num)
        num=1
        for i in range(len(nums)-1,0,-1):
            op[i]=op[i]*num
            num=num*nums[i]
        op[0]=op[0]*num
        return op
        