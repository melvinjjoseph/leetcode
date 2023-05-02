class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg=0
        for ele in nums:
            if ele==0:
                return 0
            elif ele<0:
                neg+=1
        if neg%2==1:
            return -1
        else:
            return 1
        
                
        