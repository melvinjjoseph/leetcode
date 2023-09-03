class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxleft=[0]*len(height)
        maxright=[0]*len(height)
        tmpmax=0
        for i in range(len(height)):
            maxleft[i]=tmpmax
            tmpmax=max(tmpmax,height[i])
        tmpmax=0
        for i in range(len(height)-1,-1,-1):
            maxright[i]=tmpmax
            tmpmax=max(tmpmax,height[i])
        res=0
        print(maxright)
        
        for i in range(len(height)):
            tmpmax=min(maxleft[i],maxright[i])-height[i]
            if tmpmax>0:
                res+=tmpmax
        return res
        