class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i]!=d:
                return False
        return True
        