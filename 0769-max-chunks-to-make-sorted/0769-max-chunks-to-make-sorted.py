class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk=0
        num1=0
        num2=0
        for i in range(len(arr)):
            num1+=i
            num2+=arr[i]
            if num1==num2:
                chunk+=1
        return chunk