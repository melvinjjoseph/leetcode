class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr=[]
        for l,m in zip(dist,speed):
            arr.append(l/m)
        arr.sort()
        ans=0
        for i in range(len(arr)):
            if arr[i]<=i:
                break
            ans+=1
        return ans