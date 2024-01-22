class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        chklist=[0]*(len(nums)+1)
        for i in nums:
            chklist[i]+=1
        zer=1
        two=1
        for i in range(len(chklist)):
            if chklist[i]==0:
                zer=i
            if chklist[i]==2:
                two=i
        return [two, zer]