class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour<len(dist)-1:
            return -1
        def isPossible(speed):
            c=0
            for i in range(len(dist)):
                if i==len(dist)-1:
                    c+=dist[i]/speed
                else:
                    c+=math.ceil(dist[i]/speed)
            return c<=hour
            
            
            
        l,r=1,10000000
        minSpeed=-1
        while l<=r:
            mid=(l+r)//2
            if isPossible(mid):
                minSpeed=mid
                r=mid-1
            else:
                l=mid+1
        return minSpeed