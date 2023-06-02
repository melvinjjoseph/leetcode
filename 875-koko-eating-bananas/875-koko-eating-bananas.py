class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValidNum(k):
            c=0
            for i in piles:
                c=c+math.ceil(i/k)
            if c<=h:
                return True
            return False
        
        l=1
        r=max(piles)
        while(l<=r):
            mid=(r+l)//2
            if isValidNum(mid):
                r=mid-1
            else:
                l=mid+1
        if isValidNum(mid):
            return mid 
        else:
            return mid+1
        
            
        
        
        
        
        
        
        
        
        